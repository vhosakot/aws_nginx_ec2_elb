terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = var.aws_region
}

# Create SSH key pair in AWS
resource "aws_key_pair" "nginx-key-pair" {
  key_name   = "nginx-key-pair"
  public_key = var.ssh_public_key
}

# Data Source to get default VPC in AWS
data "aws_vpc" "default" {
  default = true
} 

# Create security group to allow TCP ports 22 and 80 for SSH access and HTTP respectively
resource "aws_security_group" "nginx-security-grp" {
  name        = "nginx-security-grp"
  description = "Security group for Nginx web server"
  vpc_id      = (var.vpc_id != "" ? var.vpc_id : data.aws_vpc.default.id)

  # Allow SSH access
  ingress {
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  # Allow HTTP
  ingress {
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  } 

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags = {
    Name = "nginx-security-grp"
  }
}

# Data Source to get Ubuntu AMI image
data "aws_ami" "ubuntu2204" {
  filter {
    name   = "name"
    values = [var.ami_image_name]
  }
}

# Create EC2 instance
resource "aws_instance" "nginx-ec2" {
  ami             = data.aws_ami.ubuntu2204.id
  instance_type   = "t2.micro"
  key_name        = "nginx-key-pair"
  security_groups = ["nginx-security-grp"]
  # If Subnet ID is not provided in variables.tf, do not set subnet_id and
  # use the default Subnet ID in AWS
  subnet_id       = (var.subnet_id != "" ? var.subnet_id : null)

  # User data to install Nginx web server and add
  # static home page for Nginx. Output of user-data-nginx.sh
  # will be at /var/log/cloud-init-output.log in the EC2 instance
  user_data = "${file("user-data-nginx.sh")}"

  tags = {
    Name = "nginx-ec2"
  }
}

# Create instance Target Group for EC2 instance used by Load Balancer
resource "aws_lb_target_group" "nginx-target-grp" {
  name     = "nginx-target-grp"
  port     = 80
  protocol = "HTTP"
  vpc_id   = (var.vpc_id != "" ? var.vpc_id : data.aws_vpc.default.id)
}

# Register EC2 instance with Target Group
resource "aws_lb_target_group_attachment" "nginx-target-grp-attach" {
  target_group_arn = aws_lb_target_group.nginx-target-grp.arn
  target_id        = aws_instance.nginx-ec2.id
  port             = 80
}

# Print EC2 instance's public IP address in output
output "ec2_instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.nginx-ec2.public_ip
}

# Data source to get subnets of VPC
data "aws_subnets" "subnets" {
  filter {
    name   = "vpc-id"
    values = [(var.vpc_id != "" ? var.vpc_id : data.aws_vpc.default.id)]
  }
}

# Create Elastic Load Balancer
resource "aws_lb" "nginx-lb" {
  name               = "nginx-lb"
  internal           = false
  load_balancer_type = "application"
  ip_address_type    = "ipv4"
  security_groups    = [aws_security_group.nginx-security-grp.id]
  subnets            = data.aws_subnets.subnets.ids
}

# Create HTTP Listener on TCP port 80 for Load Balancer
resource "aws_lb_listener" "nginx-lb-listener" {
  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.nginx-target-grp.arn
  }
  load_balancer_arn = aws_lb.nginx-lb.arn
  port              = "80"
  protocol          = "HTTP"
}

# Print Load Balancer's public DNS name in output
output "lb_public_dns" {
  description = "Load Balancer's public DNS name"
  value       = aws_lb.nginx-lb.dns_name
}
