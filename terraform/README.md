#### Install Terraform on Mac

https://learn.hashicorp.com/tutorials/terraform/install-cli

```
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
brew update
brew upgrade hashicorp/tap/terraform
terraform -help
terraform -help plan
```

#### Provision using Terraform

VPC ID to create Security Group and Target Group used by Load Balancer, and Subnet ID to create EC2 instance can be optionally set for the variables `vpc_id` and `subnet_id` in `variables.tf`. If they are not set, the default VPC ID and default Subnet ID will be used.

Set AWS access keys and AWS region in `~/.aws/credentials`.

```
$ terraform init

$ terraform validate
Success! The configuration is valid.

$ terraform plan
data.aws_vpc.default: Reading...
data.aws_ami.ubuntu2204: Reading...
data.aws_vpc.default: Read complete after 0s [id=vpc-0edbd187d65482beb]
data.aws_subnets.subnets: Reading...
data.aws_subnets.subnets: Read complete after 0s [id=us-east-1]
data.aws_ami.ubuntu2204: Read complete after 1s [id=ami-052efd3df9dad4825]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_instance.nginx-ec2 will be created
  + resource "aws_instance" "nginx-ec2" {
      + ami                                  = "ami-052efd3df9dad4825"
      + arn                                  = (known after apply)
      + associate_public_ip_address          = (known after apply)
      + availability_zone                    = (known after apply)
      + cpu_core_count                       = (known after apply)
      + cpu_threads_per_core                 = (known after apply)
      + disable_api_stop                     = (known after apply)
      + disable_api_termination              = (known after apply)
      + ebs_optimized                        = (known after apply)
      + get_password_data                    = false
      + host_id                              = (known after apply)
      + host_resource_group_arn              = (known after apply)
      + id                                   = (known after apply)
      + instance_initiated_shutdown_behavior = (known after apply)
      + instance_state                       = (known after apply)
      + instance_type                        = "t2.micro"
      + ipv6_address_count                   = (known after apply)
      + ipv6_addresses                       = (known after apply)
      + key_name                             = "nginx-key-pair"
      + monitoring                           = (known after apply)
      + outpost_arn                          = (known after apply)
      + password_data                        = (known after apply)
      + placement_group                      = (known after apply)
      + placement_partition_number           = (known after apply)
      + primary_network_interface_id         = (known after apply)
      + private_dns                          = (known after apply)
      + private_ip                           = (known after apply)
      + public_dns                           = (known after apply)
      + public_ip                            = (known after apply)
      + secondary_private_ips                = (known after apply)
      + security_groups                      = [
          + "nginx-security-grp",
        ]
      + source_dest_check                    = true
      + subnet_id                            = (known after apply)
      + tags                                 = {
          + "Name" = "nginx-ec2"
        }
      + tags_all                             = {
          + "Name" = "nginx-ec2"
        }
      + tenancy                              = (known after apply)
      + user_data                            = "cde35c9c12fcd7c118915c54d146e75810da2f46"
      + user_data_base64                     = (known after apply)
      + user_data_replace_on_change          = false
      + vpc_security_group_ids               = (known after apply)

      + capacity_reservation_specification {
          + capacity_reservation_preference = (known after apply)

          + capacity_reservation_target {
              + capacity_reservation_id                 = (known after apply)
              + capacity_reservation_resource_group_arn = (known after apply)
            }
        }

      + ebs_block_device {
          + delete_on_termination = (known after apply)
          + device_name           = (known after apply)
          + encrypted             = (known after apply)
          + iops                  = (known after apply)
          + kms_key_id            = (known after apply)
          + snapshot_id           = (known after apply)
          + tags                  = (known after apply)
          + throughput            = (known after apply)
          + volume_id             = (known after apply)
          + volume_size           = (known after apply)
          + volume_type           = (known after apply)
        }

      + enclave_options {
          + enabled = (known after apply)
        }

      + ephemeral_block_device {
          + device_name  = (known after apply)
          + no_device    = (known after apply)
          + virtual_name = (known after apply)
        }

      + maintenance_options {
          + auto_recovery = (known after apply)
        }

      + metadata_options {
          + http_endpoint               = (known after apply)
          + http_put_response_hop_limit = (known after apply)
          + http_tokens                 = (known after apply)
          + instance_metadata_tags      = (known after apply)
        }

      + network_interface {
          + delete_on_termination = (known after apply)
          + device_index          = (known after apply)
          + network_card_index    = (known after apply)
          + network_interface_id  = (known after apply)
        }

      + private_dns_name_options {
          + enable_resource_name_dns_a_record    = (known after apply)
          + enable_resource_name_dns_aaaa_record = (known after apply)
          + hostname_type                        = (known after apply)
        }

      + root_block_device {
          + delete_on_termination = (known after apply)
          + device_name           = (known after apply)
          + encrypted             = (known after apply)
          + iops                  = (known after apply)
          + kms_key_id            = (known after apply)
          + tags                  = (known after apply)
          + throughput            = (known after apply)
          + volume_id             = (known after apply)
          + volume_size           = (known after apply)
          + volume_type           = (known after apply)
        }
    }

  # aws_key_pair.nginx-key-pair will be created
  + resource "aws_key_pair" "nginx-key-pair" {
      + arn             = (known after apply)
      + fingerprint     = (known after apply)
      + id              = (known after apply)
      + key_name        = "nginx-key-pair"
      + key_name_prefix = (known after apply)
      + key_pair_id     = (known after apply)
      + key_type        = (known after apply)
      + public_key      = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILkjJM0CixodNbOvBeFudqsLtINElv3qA0EmE26+mZzH vhosakot@VHOSAKOT-M-C3TN"
      + tags_all        = (known after apply)
    }

  # aws_lb.nginx-lb will be created
  + resource "aws_lb" "nginx-lb" {
      + arn                        = (known after apply)
      + arn_suffix                 = (known after apply)
      + desync_mitigation_mode     = "defensive"
      + dns_name                   = (known after apply)
      + drop_invalid_header_fields = false
      + enable_deletion_protection = false
      + enable_http2               = true
      + enable_waf_fail_open       = false
      + id                         = (known after apply)
      + idle_timeout               = 60
      + internal                   = false
      + ip_address_type            = "ipv4"
      + load_balancer_type         = "application"
      + name                       = "nginx-lb"
      + preserve_host_header       = false
      + security_groups            = (known after apply)
      + subnets                    = [
          + "subnet-092224c1441f71de6",
          + "subnet-09634b9cc5dac6992",
          + "subnet-0a603f428ebf3de12",
          + "subnet-0c376d73ba74a2ed3",
          + "subnet-0e191afc433f80918",
          + "subnet-0e1e5995fe42c90a4",
        ]
      + tags_all                   = (known after apply)
      + vpc_id                     = (known after apply)
      + zone_id                    = (known after apply)

      + subnet_mapping {
          + allocation_id        = (known after apply)
          + ipv6_address         = (known after apply)
          + outpost_id           = (known after apply)
          + private_ipv4_address = (known after apply)
          + subnet_id            = (known after apply)
        }
    }

  # aws_lb_listener.nginx-lb-listener will be created
  + resource "aws_lb_listener" "nginx-lb-listener" {
      + arn               = (known after apply)
      + id                = (known after apply)
      + load_balancer_arn = (known after apply)
      + port              = 80
      + protocol          = "HTTP"
      + ssl_policy        = (known after apply)
      + tags_all          = (known after apply)

      + default_action {
          + order            = (known after apply)
          + target_group_arn = (known after apply)
          + type             = "forward"
        }
    }

  # aws_lb_target_group.nginx-target-grp will be created
  + resource "aws_lb_target_group" "nginx-target-grp" {
      + arn                                = (known after apply)
      + arn_suffix                         = (known after apply)
      + connection_termination             = false
      + deregistration_delay               = "300"
      + id                                 = (known after apply)
      + ip_address_type                    = (known after apply)
      + lambda_multi_value_headers_enabled = false
      + load_balancing_algorithm_type      = (known after apply)
      + name                               = "nginx-target-grp"
      + port                               = 80
      + preserve_client_ip                 = (known after apply)
      + protocol                           = "HTTP"
      + protocol_version                   = (known after apply)
      + proxy_protocol_v2                  = false
      + slow_start                         = 0
      + tags_all                           = (known after apply)
      + target_type                        = "instance"
      + vpc_id                             = "vpc-0edbd187d65482beb"

      + health_check {
          + enabled             = (known after apply)
          + healthy_threshold   = (known after apply)
          + interval            = (known after apply)
          + matcher             = (known after apply)
          + path                = (known after apply)
          + port                = (known after apply)
          + protocol            = (known after apply)
          + timeout             = (known after apply)
          + unhealthy_threshold = (known after apply)
        }

      + stickiness {
          + cookie_duration = (known after apply)
          + cookie_name     = (known after apply)
          + enabled         = (known after apply)
          + type            = (known after apply)
        }
    }

  # aws_lb_target_group_attachment.nginx-target-grp-attach will be created
  + resource "aws_lb_target_group_attachment" "nginx-target-grp-attach" {
      + id               = (known after apply)
      + port             = 80
      + target_group_arn = (known after apply)
      + target_id        = (known after apply)
    }

  # aws_security_group.nginx-security-grp will be created
  + resource "aws_security_group" "nginx-security-grp" {
      + arn                    = (known after apply)
      + description            = "Security group for Nginx web server"
      + egress                 = [
          + {
              + cidr_blocks      = [
                  + "0.0.0.0/0",
                ]
              + description      = ""
              + from_port        = 0
              + ipv6_cidr_blocks = []
              + prefix_list_ids  = []
              + protocol         = "-1"
              + security_groups  = []
              + self             = false
              + to_port          = 0
            },
        ]
      + id                     = (known after apply)
      + ingress                = [
          + {
              + cidr_blocks      = [
                  + "0.0.0.0/0",
                ]
              + description      = ""
              + from_port        = 22
              + ipv6_cidr_blocks = []
              + prefix_list_ids  = []
              + protocol         = "tcp"
              + security_groups  = []
              + self             = false
              + to_port          = 22
            },
          + {
              + cidr_blocks      = [
                  + "0.0.0.0/0",
                ]
              + description      = ""
              + from_port        = 80
              + ipv6_cidr_blocks = []
              + prefix_list_ids  = []
              + protocol         = "tcp"
              + security_groups  = []
              + self             = false
              + to_port          = 80
            },
        ]
      + name                   = "nginx-security-grp"
      + name_prefix            = (known after apply)
      + owner_id               = (known after apply)
      + revoke_rules_on_delete = false
      + tags                   = {
          + "Name" = "nginx-security-grp"
        }
      + tags_all               = {
          + "Name" = "nginx-security-grp"
        }
      + vpc_id                 = "vpc-0edbd187d65482beb"
    }

Plan: 7 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + ec2_instance_public_ip = (known after apply)
  + lb_public_dns          = (known after apply)

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform
apply" now.
```

```
$ terraform apply
data.aws_vpc.default: Reading...
data.aws_ami.ubuntu2204: Reading...
data.aws_vpc.default: Read complete after 1s [id=vpc-0edbd187d65482beb]
data.aws_subnets.subnets: Reading...
data.aws_subnets.subnets: Read complete after 0s [id=us-east-1]
data.aws_ami.ubuntu2204: Read complete after 1s [id=ami-052efd3df9dad4825]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_instance.nginx-ec2 will be created
  + resource "aws_instance" "nginx-ec2" {
      + ami                                  = "ami-052efd3df9dad4825"
      + arn                                  = (known after apply)
      + associate_public_ip_address          = (known after apply)
      + availability_zone                    = (known after apply)
      + cpu_core_count                       = (known after apply)
      + cpu_threads_per_core                 = (known after apply)
      + disable_api_stop                     = (known after apply)
      + disable_api_termination              = (known after apply)
      + ebs_optimized                        = (known after apply)
      + get_password_data                    = false
      + host_id                              = (known after apply)
      + host_resource_group_arn              = (known after apply)
      + id                                   = (known after apply)
      + instance_initiated_shutdown_behavior = (known after apply)
      + instance_state                       = (known after apply)
      + instance_type                        = "t2.micro"
      + ipv6_address_count                   = (known after apply)
      + ipv6_addresses                       = (known after apply)
      + key_name                             = "nginx-key-pair"
      + monitoring                           = (known after apply)
      + outpost_arn                          = (known after apply)
      + password_data                        = (known after apply)
      + placement_group                      = (known after apply)
      + placement_partition_number           = (known after apply)
      + primary_network_interface_id         = (known after apply)
      + private_dns                          = (known after apply)
      + private_ip                           = (known after apply)
      + public_dns                           = (known after apply)
      + public_ip                            = (known after apply)
      + secondary_private_ips                = (known after apply)
      + security_groups                      = [
          + "nginx-security-grp",
        ]
      + source_dest_check                    = true
      + subnet_id                            = (known after apply)
      + tags                                 = {
          + "Name" = "nginx-ec2"
        }
      + tags_all                             = {
          + "Name" = "nginx-ec2"
        }
      + tenancy                              = (known after apply)
      + user_data                            = "cde35c9c12fcd7c118915c54d146e75810da2f46"
      + user_data_base64                     = (known after apply)
      + user_data_replace_on_change          = false
      + vpc_security_group_ids               = (known after apply)

      + capacity_reservation_specification {
          + capacity_reservation_preference = (known after apply)

          + capacity_reservation_target {
              + capacity_reservation_id                 = (known after apply)
              + capacity_reservation_resource_group_arn = (known after apply)
            }
        }

      + ebs_block_device {
          + delete_on_termination = (known after apply)
          + device_name           = (known after apply)
          + encrypted             = (known after apply)
          + iops                  = (known after apply)
          + kms_key_id            = (known after apply)
          + snapshot_id           = (known after apply)
          + tags                  = (known after apply)
          + throughput            = (known after apply)
          + volume_id             = (known after apply)
          + volume_size           = (known after apply)
          + volume_type           = (known after apply)
        }

      + enclave_options {
          + enabled = (known after apply)
        }

      + ephemeral_block_device {
          + device_name  = (known after apply)
          + no_device    = (known after apply)
          + virtual_name = (known after apply)
        }

      + maintenance_options {
          + auto_recovery = (known after apply)
        }

      + metadata_options {
          + http_endpoint               = (known after apply)
          + http_put_response_hop_limit = (known after apply)
          + http_tokens                 = (known after apply)
          + instance_metadata_tags      = (known after apply)
        }

      + network_interface {
          + delete_on_termination = (known after apply)
          + device_index          = (known after apply)
          + network_card_index    = (known after apply)
          + network_interface_id  = (known after apply)
        }

      + private_dns_name_options {
          + enable_resource_name_dns_a_record    = (known after apply)
          + enable_resource_name_dns_aaaa_record = (known after apply)
          + hostname_type                        = (known after apply)
        }

      + root_block_device {
          + delete_on_termination = (known after apply)
          + device_name           = (known after apply)
          + encrypted             = (known after apply)
          + iops                  = (known after apply)
          + kms_key_id            = (known after apply)
          + tags                  = (known after apply)
          + throughput            = (known after apply)
          + volume_id             = (known after apply)
          + volume_size           = (known after apply)
          + volume_type           = (known after apply)
        }
    }

  # aws_key_pair.nginx-key-pair will be created
  + resource "aws_key_pair" "nginx-key-pair" {
      + arn             = (known after apply)
      + fingerprint     = (known after apply)
      + id              = (known after apply)
      + key_name        = "nginx-key-pair"
      + key_name_prefix = (known after apply)
      + key_pair_id     = (known after apply)
      + key_type        = (known after apply)
      + public_key      = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILkjJM0CixodNbOvBeFudqsLtINElv3qA0EmE26+mZzH vhosakot@VHOSAKOT-M-C3TN"
      + tags_all        = (known after apply)
    }

  # aws_lb.nginx-lb will be created
  + resource "aws_lb" "nginx-lb" {
      + arn                        = (known after apply)
      + arn_suffix                 = (known after apply)
      + desync_mitigation_mode     = "defensive"
      + dns_name                   = (known after apply)
      + drop_invalid_header_fields = false
      + enable_deletion_protection = false
      + enable_http2               = true
      + enable_waf_fail_open       = false
      + id                         = (known after apply)
      + idle_timeout               = 60
      + internal                   = false
      + ip_address_type            = "ipv4"
      + load_balancer_type         = "application"
      + name                       = "nginx-lb"
      + preserve_host_header       = false
      + security_groups            = (known after apply)
      + subnets                    = [
          + "subnet-092224c1441f71de6",
          + "subnet-09634b9cc5dac6992",
          + "subnet-0a603f428ebf3de12",
          + "subnet-0c376d73ba74a2ed3",
          + "subnet-0e191afc433f80918",
          + "subnet-0e1e5995fe42c90a4",
        ]
      + tags_all                   = (known after apply)
      + vpc_id                     = (known after apply)
      + zone_id                    = (known after apply)

      + subnet_mapping {
          + allocation_id        = (known after apply)
          + ipv6_address         = (known after apply)
          + outpost_id           = (known after apply)
          + private_ipv4_address = (known after apply)
          + subnet_id            = (known after apply)
        }
    }

  # aws_lb_listener.nginx-lb-listener will be created
  + resource "aws_lb_listener" "nginx-lb-listener" {
      + arn               = (known after apply)
      + id                = (known after apply)
      + load_balancer_arn = (known after apply)
      + port              = 80
      + protocol          = "HTTP"
      + ssl_policy        = (known after apply)
      + tags_all          = (known after apply)

      + default_action {
          + order            = (known after apply)
          + target_group_arn = (known after apply)
          + type             = "forward"
        }
    }

  # aws_lb_target_group.nginx-target-grp will be created
  + resource "aws_lb_target_group" "nginx-target-grp" {
      + arn                                = (known after apply)
      + arn_suffix                         = (known after apply)
      + connection_termination             = false
      + deregistration_delay               = "300"
      + id                                 = (known after apply)
      + ip_address_type                    = (known after apply)
      + lambda_multi_value_headers_enabled = false
      + load_balancing_algorithm_type      = (known after apply)
      + name                               = "nginx-target-grp"
      + port                               = 80
      + preserve_client_ip                 = (known after apply)
      + protocol                           = "HTTP"
      + protocol_version                   = (known after apply)
      + proxy_protocol_v2                  = false
      + slow_start                         = 0
      + tags_all                           = (known after apply)
      + target_type                        = "instance"
      + vpc_id                             = "vpc-0edbd187d65482beb"

      + health_check {
          + enabled             = (known after apply)
          + healthy_threshold   = (known after apply)
          + interval            = (known after apply)
          + matcher             = (known after apply)
          + path                = (known after apply)
          + port                = (known after apply)
          + protocol            = (known after apply)
          + timeout             = (known after apply)
          + unhealthy_threshold = (known after apply)
        }

      + stickiness {
          + cookie_duration = (known after apply)
          + cookie_name     = (known after apply)
          + enabled         = (known after apply)
          + type            = (known after apply)
        }
    }

  # aws_lb_target_group_attachment.nginx-target-grp-attach will be created
  + resource "aws_lb_target_group_attachment" "nginx-target-grp-attach" {
      + id               = (known after apply)
      + port             = 80
      + target_group_arn = (known after apply)
      + target_id        = (known after apply)
    }

  # aws_security_group.nginx-security-grp will be created
  + resource "aws_security_group" "nginx-security-grp" {
      + arn                    = (known after apply)
      + description            = "Security group for Nginx web server"
      + egress                 = [
          + {
              + cidr_blocks      = [
                  + "0.0.0.0/0",
                ]
              + description      = ""
              + from_port        = 0
              + ipv6_cidr_blocks = []
              + prefix_list_ids  = []
              + protocol         = "-1"
              + security_groups  = []
              + self             = false
              + to_port          = 0
            },
        ]
      + id                     = (known after apply)
      + ingress                = [
          + {
              + cidr_blocks      = [
                  + "0.0.0.0/0",
                ]
              + description      = ""
              + from_port        = 22
              + ipv6_cidr_blocks = []
              + prefix_list_ids  = []
              + protocol         = "tcp"
              + security_groups  = []
              + self             = false
              + to_port          = 22
            },
          + {
              + cidr_blocks      = [
                  + "0.0.0.0/0",
                ]
              + description      = ""
              + from_port        = 80
              + ipv6_cidr_blocks = []
              + prefix_list_ids  = []
              + protocol         = "tcp"
              + security_groups  = []
              + self             = false
              + to_port          = 80
            },
        ]
      + name                   = "nginx-security-grp"
      + name_prefix            = (known after apply)
      + owner_id               = (known after apply)
      + revoke_rules_on_delete = false
      + tags                   = {
          + "Name" = "nginx-security-grp"
        }
      + tags_all               = {
          + "Name" = "nginx-security-grp"
        }
      + vpc_id                 = "vpc-0edbd187d65482beb"
    }

Plan: 7 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + ec2_instance_public_ip = (known after apply)
  + lb_public_dns          = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

aws_key_pair.nginx-key-pair: Creating...
aws_lb_target_group.nginx-target-grp: Creating...
aws_security_group.nginx-security-grp: Creating...
aws_instance.nginx-ec2: Creating...
aws_key_pair.nginx-key-pair: Creation complete after 0s [id=nginx-key-pair]
aws_lb_target_group.nginx-target-grp: Creation complete after 1s [id=arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895]
aws_security_group.nginx-security-grp: Creation complete after 3s [id=sg-02bf191b967d52571]
aws_lb.nginx-lb: Creating...
aws_instance.nginx-ec2: Still creating... [10s elapsed]
aws_lb.nginx-lb: Still creating... [10s elapsed]
aws_instance.nginx-ec2: Still creating... [20s elapsed]
aws_lb.nginx-lb: Still creating... [20s elapsed]
aws_instance.nginx-ec2: Still creating... [30s elapsed]
aws_lb.nginx-lb: Still creating... [30s elapsed]
aws_instance.nginx-ec2: Creation complete after 35s [id=i-02400694616269e82]
aws_lb_target_group_attachment.nginx-target-grp-attach: Creating...
aws_lb_target_group_attachment.nginx-target-grp-attach: Creation complete after 0s [id=arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895-20220919181433949300000001]
aws_lb.nginx-lb: Still creating... [40s elapsed]
aws_lb.nginx-lb: Still creating... [50s elapsed]
aws_lb.nginx-lb: Still creating... [1m0s elapsed]
aws_lb.nginx-lb: Still creating... [1m10s elapsed]
aws_lb.nginx-lb: Still creating... [1m20s elapsed]
aws_lb.nginx-lb: Still creating... [1m30s elapsed]
aws_lb.nginx-lb: Still creating... [1m40s elapsed]
aws_lb.nginx-lb: Still creating... [1m50s elapsed]
aws_lb.nginx-lb: Still creating... [2m0s elapsed]
aws_lb.nginx-lb: Still creating... [2m10s elapsed]
aws_lb.nginx-lb: Creation complete after 2m13s [id=arn:aws:elasticloadbalancing:us-east-1:672534531507:loadbalancer/app/nginx-lb/5139d94031f6dda2]
aws_lb_listener.nginx-lb-listener: Creating...
aws_lb_listener.nginx-lb-listener: Creation complete after 0s [id=arn:aws:elasticloadbalancing:us-east-1:672534531507:listener/app/nginx-lb/5139d94031f6dda2/eab6a8eae1fc644a]

Apply complete! Resources: 7 added, 0 changed, 0 destroyed.

Outputs:

ec2_instance_public_ip = "54.196.249.15"
lb_public_dns = "nginx-lb-473866313.us-east-1.elb.amazonaws.com"
```

```
$ ssh ubuntu@54.196.249.15
ubuntu@ip-172-31-17-49:~$ tail -f /var/log/cloud-init-output.log 
      Tasks: 2 (limit: 1146)
     Memory: 5.3M
        CPU: 24ms
     CGroup: /system.slice/nginx.service
             ├─14743 "nginx: master process /usr/sbin/nginx -g daemon on; master_process on;"
             └─14748 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""

Sep 19 18:16:26 ip-172-31-17-49 systemd[1]: Starting A high performance web server and a reverse proxy server...
Sep 19 18:16:26 ip-172-31-17-49 systemd[1]: Started A high performance web server and a reverse proxy server.
Cloud-init v. 22.2-0ubuntu1~22.04.1 finished at Mon, 19 Sep 2022 18:16:31 +0000. Datasource DataSourceEc2Local.  Up 123.03 seconds
^C
ubuntu@ip-172-31-17-49:~$ exit
```

```
curl http://nginx-lb-473866313.us-east-1.elb.amazonaws.com
<!DOCTYPE html><html><body><h1>Cisco SPL</h1></body></html>
```

```
$ terraform state list
data.aws_ami.ubuntu2204
data.aws_subnets.subnets
data.aws_vpc.default
aws_instance.nginx-ec2
aws_key_pair.nginx-key-pair
aws_lb.nginx-lb
aws_lb_listener.nginx-lb-listener
aws_lb_target_group.nginx-target-grp
aws_lb_target_group_attachment.nginx-target-grp-attach
aws_security_group.nginx-security-grp
```

```
$ terraform show
# aws_instance.nginx-ec2:
resource "aws_instance" "nginx-ec2" {
    ami                                  = "ami-052efd3df9dad4825"
    arn                                  = "arn:aws:ec2:us-east-1:672534531507:instance/i-02400694616269e82"
    associate_public_ip_address          = true
    availability_zone                    = "us-east-1d"
    cpu_core_count                       = 1
    cpu_threads_per_core                 = 1
    disable_api_stop                     = false
    disable_api_termination              = false
    ebs_optimized                        = false
    get_password_data                    = false
    hibernation                          = false
    id                                   = "i-02400694616269e82"
    instance_initiated_shutdown_behavior = "stop"
    instance_state                       = "running"
    instance_type                        = "t2.micro"
    ipv6_address_count                   = 0
    ipv6_addresses                       = []
    key_name                             = "nginx-key-pair"
    monitoring                           = false
    primary_network_interface_id         = "eni-0b12553b2273359c8"
    private_dns                          = "ip-172-31-17-49.ec2.internal"
    private_ip                           = "172.31.17.49"
    public_dns                           = "ec2-54-196-249-15.compute-1.amazonaws.com"
    public_ip                            = "54.196.249.15"
    secondary_private_ips                = []
    security_groups                      = [
        "nginx-security-grp",
    ]
    source_dest_check                    = true
    subnet_id                            = "subnet-09634b9cc5dac6992"
    tags                                 = {
        "Name" = "nginx-ec2"
    }
    tags_all                             = {
        "Name" = "nginx-ec2"
    }
    tenancy                              = "default"
    user_data                            = "cde35c9c12fcd7c118915c54d146e75810da2f46"
    user_data_replace_on_change          = false
    vpc_security_group_ids               = [
        "sg-02bf191b967d52571",
    ]

    capacity_reservation_specification {
        capacity_reservation_preference = "open"
    }

    credit_specification {
        cpu_credits = "standard"
    }

    enclave_options {
        enabled = false
    }

    maintenance_options {
        auto_recovery = "default"
    }

    metadata_options {
        http_endpoint               = "enabled"
        http_put_response_hop_limit = 1
        http_tokens                 = "optional"
        instance_metadata_tags      = "disabled"
    }

    private_dns_name_options {
        enable_resource_name_dns_a_record    = false
        enable_resource_name_dns_aaaa_record = false
        hostname_type                        = "ip-name"
    }

    root_block_device {
        delete_on_termination = true
        device_name           = "/dev/sda1"
        encrypted             = false
        iops                  = 100
        tags                  = {}
        throughput            = 0
        volume_id             = "vol-0a9308bd4ffaa3fec"
        volume_size           = 8
        volume_type           = "gp2"
    }
}

# aws_key_pair.nginx-key-pair:
resource "aws_key_pair" "nginx-key-pair" {
    arn         = "arn:aws:ec2:us-east-1:672534531507:key-pair/nginx-key-pair"
    fingerprint = "a1tkkTgj8FYwR3caF81JMefRlpABwGFxc8miekhB54A="
    id          = "nginx-key-pair"
    key_name    = "nginx-key-pair"
    key_pair_id = "key-0dd6714964920cfe7"
    key_type    = "ed25519"
    public_key  = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILkjJM0CixodNbOvBeFudqsLtINElv3qA0EmE26+mZzH vhosakot@VHOSAKOT-M-C3TN"
    tags_all    = {}
}

# aws_lb.nginx-lb:
resource "aws_lb" "nginx-lb" {
    arn                        = "arn:aws:elasticloadbalancing:us-east-1:672534531507:loadbalancer/app/nginx-lb/5139d94031f6dda2"
    arn_suffix                 = "app/nginx-lb/5139d94031f6dda2"
    desync_mitigation_mode     = "defensive"
    dns_name                   = "nginx-lb-473866313.us-east-1.elb.amazonaws.com"
    drop_invalid_header_fields = false
    enable_deletion_protection = false
    enable_http2               = true
    enable_waf_fail_open       = false
    id                         = "arn:aws:elasticloadbalancing:us-east-1:672534531507:loadbalancer/app/nginx-lb/5139d94031f6dda2"
    idle_timeout               = 60
    internal                   = false
    ip_address_type            = "ipv4"
    load_balancer_type         = "application"
    name                       = "nginx-lb"
    preserve_host_header       = false
    security_groups            = [
        "sg-02bf191b967d52571",
    ]
    subnets                    = [
        "subnet-092224c1441f71de6",
        "subnet-09634b9cc5dac6992",
        "subnet-0a603f428ebf3de12",
        "subnet-0c376d73ba74a2ed3",
        "subnet-0e191afc433f80918",
        "subnet-0e1e5995fe42c90a4",
    ]
    tags_all                   = {}
    vpc_id                     = "vpc-0edbd187d65482beb"
    zone_id                    = "Z35SXDOTRQ7X7K"

    access_logs {
        enabled = false
    }

    subnet_mapping {
        subnet_id = "subnet-092224c1441f71de6"
    }
    subnet_mapping {
        subnet_id = "subnet-09634b9cc5dac6992"
    }
    subnet_mapping {
        subnet_id = "subnet-0a603f428ebf3de12"
    }
    subnet_mapping {
        subnet_id = "subnet-0c376d73ba74a2ed3"
    }
    subnet_mapping {
        subnet_id = "subnet-0e191afc433f80918"
    }
    subnet_mapping {
        subnet_id = "subnet-0e1e5995fe42c90a4"
    }
}

# aws_lb_listener.nginx-lb-listener:
resource "aws_lb_listener" "nginx-lb-listener" {
    arn               = "arn:aws:elasticloadbalancing:us-east-1:672534531507:listener/app/nginx-lb/5139d94031f6dda2/eab6a8eae1fc644a"
    id                = "arn:aws:elasticloadbalancing:us-east-1:672534531507:listener/app/nginx-lb/5139d94031f6dda2/eab6a8eae1fc644a"
    load_balancer_arn = "arn:aws:elasticloadbalancing:us-east-1:672534531507:loadbalancer/app/nginx-lb/5139d94031f6dda2"
    port              = 80
    protocol          = "HTTP"
    tags_all          = {}

    default_action {
        order            = 1
        target_group_arn = "arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895"
        type             = "forward"
    }
}

# aws_lb_target_group.nginx-target-grp:
resource "aws_lb_target_group" "nginx-target-grp" {
    arn                                = "arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895"
    arn_suffix                         = "targetgroup/nginx-target-grp/eaa304643ab02895"
    connection_termination             = false
    deregistration_delay               = "300"
    id                                 = "arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895"
    lambda_multi_value_headers_enabled = false
    load_balancing_algorithm_type      = "round_robin"
    name                               = "nginx-target-grp"
    port                               = 80
    protocol                           = "HTTP"
    protocol_version                   = "HTTP1"
    proxy_protocol_v2                  = false
    slow_start                         = 0
    tags_all                           = {}
    target_type                        = "instance"
    vpc_id                             = "vpc-0edbd187d65482beb"

    health_check {
        enabled             = true
        healthy_threshold   = 5
        interval            = 30
        matcher             = "200"
        path                = "/"
        port                = "traffic-port"
        protocol            = "HTTP"
        timeout             = 5
        unhealthy_threshold = 2
    }

    stickiness {
        cookie_duration = 86400
        enabled         = false
        type            = "lb_cookie"
    }
}

# aws_lb_target_group_attachment.nginx-target-grp-attach:
resource "aws_lb_target_group_attachment" "nginx-target-grp-attach" {
    id               = "arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895-20220919181433949300000001"
    port             = 80
    target_group_arn = "arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895"
    target_id        = "i-02400694616269e82"
}

# aws_security_group.nginx-security-grp:
resource "aws_security_group" "nginx-security-grp" {
    arn                    = "arn:aws:ec2:us-east-1:672534531507:security-group/sg-02bf191b967d52571"
    description            = "Security group for Nginx web server"
    egress                 = [
        {
            cidr_blocks      = [
                "0.0.0.0/0",
            ]
            description      = ""
            from_port        = 0
            ipv6_cidr_blocks = []
            prefix_list_ids  = []
            protocol         = "-1"
            security_groups  = []
            self             = false
            to_port          = 0
        },
    ]
    id                     = "sg-02bf191b967d52571"
    ingress                = [
        {
            cidr_blocks      = [
                "0.0.0.0/0",
            ]
            description      = ""
            from_port        = 22
            ipv6_cidr_blocks = []
            prefix_list_ids  = []
            protocol         = "tcp"
            security_groups  = []
            self             = false
            to_port          = 22
        },
        {
            cidr_blocks      = [
                "0.0.0.0/0",
            ]
            description      = ""
            from_port        = 80
            ipv6_cidr_blocks = []
            prefix_list_ids  = []
            protocol         = "tcp"
            security_groups  = []
            self             = false
            to_port          = 80
        },
    ]
    name                   = "nginx-security-grp"
    owner_id               = "672534531507"
    revoke_rules_on_delete = false
    tags                   = {
        "Name" = "nginx-security-grp"
    }
    tags_all               = {
        "Name" = "nginx-security-grp"
    }
    vpc_id                 = "vpc-0edbd187d65482beb"
}

# data.aws_ami.ubuntu2204:
data "aws_ami" "ubuntu2204" {
    architecture          = "x86_64"
    arn                   = "arn:aws:ec2:us-east-1::image/ami-052efd3df9dad4825"
    block_device_mappings = [
        {
            device_name  = "/dev/sda1"
            ebs          = {
                "delete_on_termination" = "true"
                "encrypted"             = "false"
                "iops"                  = "0"
                "snapshot_id"           = "snap-02d9369affc74b4f8"
                "throughput"            = "0"
                "volume_size"           = "8"
                "volume_type"           = "gp2"
            }
            no_device    = ""
            virtual_name = ""
        },
        {
            device_name  = "/dev/sdb"
            ebs          = {}
            no_device    = ""
            virtual_name = "ephemeral0"
        },
        {
            device_name  = "/dev/sdc"
            ebs          = {}
            no_device    = ""
            virtual_name = "ephemeral1"
        },
    ]
    creation_date         = "2022-06-09T12:20:41.000Z"
    deprecation_time      = "2024-06-09T12:20:41.000Z"
    description           = "Canonical, Ubuntu, 22.04 LTS, amd64 jammy image build on 2022-06-09"
    ena_support           = true
    hypervisor            = "xen"
    id                    = "ami-052efd3df9dad4825"
    image_id              = "ami-052efd3df9dad4825"
    image_location        = "amazon/ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-20220609"
    image_owner_alias     = "amazon"
    image_type            = "machine"
    include_deprecated    = false
    most_recent           = false
    name                  = "ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-20220609"
    owner_id              = "099720109477"
    platform_details      = "Linux/UNIX"
    product_codes         = []
    public                = true
    root_device_name      = "/dev/sda1"
    root_device_type      = "ebs"
    root_snapshot_id      = "snap-02d9369affc74b4f8"
    sriov_net_support     = "simple"
    state                 = "available"
    state_reason          = {
        "code"    = "UNSET"
        "message" = "UNSET"
    }
    tags                  = {}
    usage_operation       = "RunInstances"
    virtualization_type   = "hvm"

    filter {
        name   = "name"
        values = [
            "*ubuntu-jammy-22.04-amd64-server-20220609*",
        ]
    }
}

# data.aws_subnets.subnets:
data "aws_subnets" "subnets" {
    id  = "us-east-1"
    ids = [
        "subnet-092224c1441f71de6",
        "subnet-0e1e5995fe42c90a4",
        "subnet-0c376d73ba74a2ed3",
        "subnet-0e191afc433f80918",
        "subnet-0a603f428ebf3de12",
        "subnet-09634b9cc5dac6992",
    ]

    filter {
        name   = "vpc-id"
        values = [
            "vpc-0edbd187d65482beb",
        ]
    }
}

# data.aws_vpc.default:
data "aws_vpc" "default" {
    arn                     = "arn:aws:ec2:us-east-1:672534531507:vpc/vpc-0edbd187d65482beb"
    cidr_block              = "172.31.0.0/16"
    cidr_block_associations = [
        {
            association_id = "vpc-cidr-assoc-043980a3f635e96c7"
            cidr_block     = "172.31.0.0/16"
            state          = "associated"
        },
    ]
    default                 = true
    dhcp_options_id         = "dopt-040b4072303ce6850"
    enable_dns_hostnames    = true
    enable_dns_support      = true
    id                      = "vpc-0edbd187d65482beb"
    instance_tenancy        = "default"
    main_route_table_id     = "rtb-0b6a6d59aeb913894"
    owner_id                = "672534531507"
    tags                    = {}
}


Outputs:

ec2_instance_public_ip = "54.196.249.15"
lb_public_dns = "nginx-lb-473866313.us-east-1.elb.amazonaws.com"
```

```
$ terraform state pull
{
  "version": 4,
  "terraform_version": "1.2.9",
  "serial": 274,
  "lineage": "58e11a69-a5c0-b3bd-37a8-768bed735998",
  "outputs": {
    "ec2_instance_public_ip": {
      "value": "54.196.249.15",
      "type": "string"
    },
    "lb_public_dns": {
      "value": "nginx-lb-473866313.us-east-1.elb.amazonaws.com",
      "type": "string"
    }
  },
  "resources": [
    {
      "mode": "data",
      "type": "aws_ami",
      "name": "ubuntu2204",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "architecture": "x86_64",
            "arn": "arn:aws:ec2:us-east-1::image/ami-052efd3df9dad4825",
            "block_device_mappings": [
              {
                "device_name": "/dev/sda1",
                "ebs": {
                  "delete_on_termination": "true",
                  "encrypted": "false",
                  "iops": "0",
                  "snapshot_id": "snap-02d9369affc74b4f8",
                  "throughput": "0",
                  "volume_size": "8",
                  "volume_type": "gp2"
                },
                "no_device": "",
                "virtual_name": ""
              },
              {
                "device_name": "/dev/sdb",
                "ebs": {},
                "no_device": "",
                "virtual_name": "ephemeral0"
              },
              {
                "device_name": "/dev/sdc",
                "ebs": {},
                "no_device": "",
                "virtual_name": "ephemeral1"
              }
            ],
            "boot_mode": "",
            "creation_date": "2022-06-09T12:20:41.000Z",
            "deprecation_time": "2024-06-09T12:20:41.000Z",
            "description": "Canonical, Ubuntu, 22.04 LTS, amd64 jammy image build on 2022-06-09",
            "ena_support": true,
            "executable_users": null,
            "filter": [
              {
                "name": "name",
                "values": [
                  "*ubuntu-jammy-22.04-amd64-server-20220609*"
                ]
              }
            ],
            "hypervisor": "xen",
            "id": "ami-052efd3df9dad4825",
            "image_id": "ami-052efd3df9dad4825",
            "image_location": "amazon/ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-20220609",
            "image_owner_alias": "amazon",
            "image_type": "machine",
            "include_deprecated": false,
            "kernel_id": "",
            "most_recent": false,
            "name": "ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-20220609",
            "name_regex": null,
            "owner_id": "099720109477",
            "owners": null,
            "platform": "",
            "platform_details": "Linux/UNIX",
            "product_codes": [],
            "public": true,
            "ramdisk_id": "",
            "root_device_name": "/dev/sda1",
            "root_device_type": "ebs",
            "root_snapshot_id": "snap-02d9369affc74b4f8",
            "sriov_net_support": "simple",
            "state": "available",
            "state_reason": {
              "code": "UNSET",
              "message": "UNSET"
            },
            "tags": {},
            "timeouts": null,
            "tpm_support": "",
            "usage_operation": "RunInstances",
            "virtualization_type": "hvm"
          },
          "sensitive_attributes": []
        }
      ]
    },
    {
      "mode": "data",
      "type": "aws_subnets",
      "name": "subnets",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "filter": [
              {
                "name": "vpc-id",
                "values": [
                  "vpc-0edbd187d65482beb"
                ]
              }
            ],
            "id": "us-east-1",
            "ids": [
              "subnet-092224c1441f71de6",
              "subnet-0e1e5995fe42c90a4",
              "subnet-0c376d73ba74a2ed3",
              "subnet-0e191afc433f80918",
              "subnet-0a603f428ebf3de12",
              "subnet-09634b9cc5dac6992"
            ],
            "tags": null,
            "timeouts": null
          },
          "sensitive_attributes": []
        }
      ]
    },
    {
      "mode": "data",
      "type": "aws_vpc",
      "name": "default",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "arn": "arn:aws:ec2:us-east-1:672534531507:vpc/vpc-0edbd187d65482beb",
            "cidr_block": "172.31.0.0/16",
            "cidr_block_associations": [
              {
                "association_id": "vpc-cidr-assoc-043980a3f635e96c7",
                "cidr_block": "172.31.0.0/16",
                "state": "associated"
              }
            ],
            "default": true,
            "dhcp_options_id": "dopt-040b4072303ce6850",
            "enable_dns_hostnames": true,
            "enable_dns_support": true,
            "filter": null,
            "id": "vpc-0edbd187d65482beb",
            "instance_tenancy": "default",
            "ipv6_association_id": "",
            "ipv6_cidr_block": "",
            "main_route_table_id": "rtb-0b6a6d59aeb913894",
            "owner_id": "672534531507",
            "state": null,
            "tags": {},
            "timeouts": null
          },
          "sensitive_attributes": []
        }
      ]
    },
    {
      "mode": "managed",
      "type": "aws_instance",
      "name": "nginx-ec2",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 1,
          "attributes": {
            "ami": "ami-052efd3df9dad4825",
            "arn": "arn:aws:ec2:us-east-1:672534531507:instance/i-02400694616269e82",
            "associate_public_ip_address": true,
            "availability_zone": "us-east-1d",
            "capacity_reservation_specification": [
              {
                "capacity_reservation_preference": "open",
                "capacity_reservation_target": []
              }
            ],
            "cpu_core_count": 1,
            "cpu_threads_per_core": 1,
            "credit_specification": [
              {
                "cpu_credits": "standard"
              }
            ],
            "disable_api_stop": false,
            "disable_api_termination": false,
            "ebs_block_device": [],
            "ebs_optimized": false,
            "enclave_options": [
              {
                "enabled": false
              }
            ],
            "ephemeral_block_device": [],
            "get_password_data": false,
            "hibernation": false,
            "host_id": null,
            "host_resource_group_arn": null,
            "iam_instance_profile": "",
            "id": "i-02400694616269e82",
            "instance_initiated_shutdown_behavior": "stop",
            "instance_state": "running",
            "instance_type": "t2.micro",
            "ipv6_address_count": 0,
            "ipv6_addresses": [],
            "key_name": "nginx-key-pair",
            "launch_template": [],
            "maintenance_options": [
              {
                "auto_recovery": "default"
              }
            ],
            "metadata_options": [
              {
                "http_endpoint": "enabled",
                "http_put_response_hop_limit": 1,
                "http_tokens": "optional",
                "instance_metadata_tags": "disabled"
              }
            ],
            "monitoring": false,
            "network_interface": [],
            "outpost_arn": "",
            "password_data": "",
            "placement_group": "",
            "placement_partition_number": null,
            "primary_network_interface_id": "eni-0b12553b2273359c8",
            "private_dns": "ip-172-31-17-49.ec2.internal",
            "private_dns_name_options": [
              {
                "enable_resource_name_dns_a_record": false,
                "enable_resource_name_dns_aaaa_record": false,
                "hostname_type": "ip-name"
              }
            ],
            "private_ip": "172.31.17.49",
            "public_dns": "ec2-54-196-249-15.compute-1.amazonaws.com",
            "public_ip": "54.196.249.15",
            "root_block_device": [
              {
                "delete_on_termination": true,
                "device_name": "/dev/sda1",
                "encrypted": false,
                "iops": 100,
                "kms_key_id": "",
                "tags": {},
                "throughput": 0,
                "volume_id": "vol-0a9308bd4ffaa3fec",
                "volume_size": 8,
                "volume_type": "gp2"
              }
            ],
            "secondary_private_ips": [],
            "security_groups": [
              "nginx-security-grp"
            ],
            "source_dest_check": true,
            "subnet_id": "subnet-09634b9cc5dac6992",
            "tags": {
              "Name": "nginx-ec2"
            },
            "tags_all": {
              "Name": "nginx-ec2"
            },
            "tenancy": "default",
            "timeouts": null,
            "user_data": "cde35c9c12fcd7c118915c54d146e75810da2f46",
            "user_data_base64": null,
            "user_data_replace_on_change": false,
            "volume_tags": null,
            "vpc_security_group_ids": [
              "sg-02bf191b967d52571"
            ]
          },
          "sensitive_attributes": [],
          "private": "eyJlMmJmYjczMC1lY2FhLTExZTYtOGY4OC0zNDM2M2JjN2M0YzAiOnsiY3JlYXRlIjo2MDAwMDAwMDAwMDAsImRlbGV0ZSI6MTIwMDAwMDAwMDAwMCwidXBkYXRlIjo2MDAwMDAwMDAwMDB9LCJzY2hlbWFfdmVyc2lvbiI6IjEifQ==",
          "dependencies": [
            "data.aws_ami.ubuntu2204"
          ]
        }
      ]
    },
    {
      "mode": "managed",
      "type": "aws_key_pair",
      "name": "nginx-key-pair",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 1,
          "attributes": {
            "arn": "arn:aws:ec2:us-east-1:672534531507:key-pair/nginx-key-pair",
            "fingerprint": "a1tkkTgj8FYwR3caF81JMefRlpABwGFxc8miekhB54A=",
            "id": "nginx-key-pair",
            "key_name": "nginx-key-pair",
            "key_name_prefix": "",
            "key_pair_id": "key-0dd6714964920cfe7",
            "key_type": "ed25519",
            "public_key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILkjJM0CixodNbOvBeFudqsLtINElv3qA0EmE26+mZzH vhosakot@VHOSAKOT-M-C3TN",
            "tags": null,
            "tags_all": {}
          },
          "sensitive_attributes": [],
          "private": "eyJzY2hlbWFfdmVyc2lvbiI6IjEifQ=="
        }
      ]
    },
    {
      "mode": "managed",
      "type": "aws_lb",
      "name": "nginx-lb",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "access_logs": [
              {
                "bucket": "",
                "enabled": false,
                "prefix": ""
              }
            ],
            "arn": "arn:aws:elasticloadbalancing:us-east-1:672534531507:loadbalancer/app/nginx-lb/5139d94031f6dda2",
            "arn_suffix": "app/nginx-lb/5139d94031f6dda2",
            "customer_owned_ipv4_pool": "",
            "desync_mitigation_mode": "defensive",
            "dns_name": "nginx-lb-473866313.us-east-1.elb.amazonaws.com",
            "drop_invalid_header_fields": false,
            "enable_cross_zone_load_balancing": null,
            "enable_deletion_protection": false,
            "enable_http2": true,
            "enable_waf_fail_open": false,
            "id": "arn:aws:elasticloadbalancing:us-east-1:672534531507:loadbalancer/app/nginx-lb/5139d94031f6dda2",
            "idle_timeout": 60,
            "internal": false,
            "ip_address_type": "ipv4",
            "load_balancer_type": "application",
            "name": "nginx-lb",
            "name_prefix": null,
            "preserve_host_header": false,
            "security_groups": [
              "sg-02bf191b967d52571"
            ],
            "subnet_mapping": [
              {
                "allocation_id": "",
                "ipv6_address": "",
                "outpost_id": "",
                "private_ipv4_address": "",
                "subnet_id": "subnet-092224c1441f71de6"
              },
              {
                "allocation_id": "",
                "ipv6_address": "",
                "outpost_id": "",
                "private_ipv4_address": "",
                "subnet_id": "subnet-09634b9cc5dac6992"
              },
              {
                "allocation_id": "",
                "ipv6_address": "",
                "outpost_id": "",
                "private_ipv4_address": "",
                "subnet_id": "subnet-0a603f428ebf3de12"
              },
              {
                "allocation_id": "",
                "ipv6_address": "",
                "outpost_id": "",
                "private_ipv4_address": "",
                "subnet_id": "subnet-0c376d73ba74a2ed3"
              },
              {
                "allocation_id": "",
                "ipv6_address": "",
                "outpost_id": "",
                "private_ipv4_address": "",
                "subnet_id": "subnet-0e191afc433f80918"
              },
              {
                "allocation_id": "",
                "ipv6_address": "",
                "outpost_id": "",
                "private_ipv4_address": "",
                "subnet_id": "subnet-0e1e5995fe42c90a4"
              }
            ],
            "subnets": [
              "subnet-092224c1441f71de6",
              "subnet-09634b9cc5dac6992",
              "subnet-0a603f428ebf3de12",
              "subnet-0c376d73ba74a2ed3",
              "subnet-0e191afc433f80918",
              "subnet-0e1e5995fe42c90a4"
            ],
            "tags": null,
            "tags_all": {},
            "timeouts": null,
            "vpc_id": "vpc-0edbd187d65482beb",
            "zone_id": "Z35SXDOTRQ7X7K"
          },
          "sensitive_attributes": [],
          "private": "eyJlMmJmYjczMC1lY2FhLTExZTYtOGY4OC0zNDM2M2JjN2M0YzAiOnsiY3JlYXRlIjo2MDAwMDAwMDAwMDAsImRlbGV0ZSI6NjAwMDAwMDAwMDAwLCJ1cGRhdGUiOjYwMDAwMDAwMDAwMH19",
          "dependencies": [
            "aws_security_group.nginx-security-grp",
            "data.aws_subnets.subnets",
            "data.aws_vpc.default"
          ]
        }
      ]
    },
    {
      "mode": "managed",
      "type": "aws_lb_listener",
      "name": "nginx-lb-listener",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "alpn_policy": null,
            "arn": "arn:aws:elasticloadbalancing:us-east-1:672534531507:listener/app/nginx-lb/5139d94031f6dda2/eab6a8eae1fc644a",
            "certificate_arn": null,
            "default_action": [
              {
                "authenticate_cognito": [],
                "authenticate_oidc": [],
                "fixed_response": [],
                "forward": [],
                "order": 1,
                "redirect": [],
                "target_group_arn": "arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895",
                "type": "forward"
              }
            ],
            "id": "arn:aws:elasticloadbalancing:us-east-1:672534531507:listener/app/nginx-lb/5139d94031f6dda2/eab6a8eae1fc644a",
            "load_balancer_arn": "arn:aws:elasticloadbalancing:us-east-1:672534531507:loadbalancer/app/nginx-lb/5139d94031f6dda2",
            "port": 80,
            "protocol": "HTTP",
            "ssl_policy": "",
            "tags": null,
            "tags_all": {},
            "timeouts": null
          },
          "sensitive_attributes": [],
          "private": "eyJlMmJmYjczMC1lY2FhLTExZTYtOGY4OC0zNDM2M2JjN2M0YzAiOnsicmVhZCI6NjAwMDAwMDAwMDAwfX0=",
          "dependencies": [
            "aws_lb.nginx-lb",
            "aws_lb_target_group.nginx-target-grp",
            "aws_security_group.nginx-security-grp",
            "data.aws_subnets.subnets",
            "data.aws_vpc.default"
          ]
        }
      ]
    },
    {
      "mode": "managed",
      "type": "aws_lb_target_group",
      "name": "nginx-target-grp",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "arn": "arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895",
            "arn_suffix": "targetgroup/nginx-target-grp/eaa304643ab02895",
            "connection_termination": false,
            "deregistration_delay": "300",
            "health_check": [
              {
                "enabled": true,
                "healthy_threshold": 5,
                "interval": 30,
                "matcher": "200",
                "path": "/",
                "port": "traffic-port",
                "protocol": "HTTP",
                "timeout": 5,
                "unhealthy_threshold": 2
              }
            ],
            "id": "arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895",
            "ip_address_type": null,
            "lambda_multi_value_headers_enabled": false,
            "load_balancing_algorithm_type": "round_robin",
            "name": "nginx-target-grp",
            "name_prefix": null,
            "port": 80,
            "preserve_client_ip": null,
            "protocol": "HTTP",
            "protocol_version": "HTTP1",
            "proxy_protocol_v2": false,
            "slow_start": 0,
            "stickiness": [
              {
                "cookie_duration": 86400,
                "cookie_name": "",
                "enabled": false,
                "type": "lb_cookie"
              }
            ],
            "tags": null,
            "tags_all": {},
            "target_type": "instance",
            "vpc_id": "vpc-0edbd187d65482beb"
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "data.aws_vpc.default"
          ]
        }
      ]
    },
    {
      "mode": "managed",
      "type": "aws_lb_target_group_attachment",
      "name": "nginx-target-grp-attach",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "availability_zone": null,
            "id": "arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895-20220919181433949300000001",
            "port": 80,
            "target_group_arn": "arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895",
            "target_id": "i-02400694616269e82"
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "aws_instance.nginx-ec2",
            "aws_lb_target_group.nginx-target-grp",
            "data.aws_ami.ubuntu2204",
            "data.aws_vpc.default"
          ]
        }
      ]
    },
    {
      "mode": "managed",
      "type": "aws_security_group",
      "name": "nginx-security-grp",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 1,
          "attributes": {
            "arn": "arn:aws:ec2:us-east-1:672534531507:security-group/sg-02bf191b967d52571",
            "description": "Security group for Nginx web server",
            "egress": [
              {
                "cidr_blocks": [
                  "0.0.0.0/0"
                ],
                "description": "",
                "from_port": 0,
                "ipv6_cidr_blocks": [],
                "prefix_list_ids": [],
                "protocol": "-1",
                "security_groups": [],
                "self": false,
                "to_port": 0
              }
            ],
            "id": "sg-02bf191b967d52571",
            "ingress": [
              {
                "cidr_blocks": [
                  "0.0.0.0/0"
                ],
                "description": "",
                "from_port": 22,
                "ipv6_cidr_blocks": [],
                "prefix_list_ids": [],
                "protocol": "tcp",
                "security_groups": [],
                "self": false,
                "to_port": 22
              },
              {
                "cidr_blocks": [
                  "0.0.0.0/0"
                ],
                "description": "",
                "from_port": 80,
                "ipv6_cidr_blocks": [],
                "prefix_list_ids": [],
                "protocol": "tcp",
                "security_groups": [],
                "self": false,
                "to_port": 80
              }
            ],
            "name": "nginx-security-grp",
            "name_prefix": "",
            "owner_id": "672534531507",
            "revoke_rules_on_delete": false,
            "tags": {
              "Name": "nginx-security-grp"
            },
            "tags_all": {
              "Name": "nginx-security-grp"
            },
            "timeouts": null,
            "vpc_id": "vpc-0edbd187d65482beb"
          },
          "sensitive_attributes": [],
          "private": "eyJlMmJmYjczMC1lY2FhLTExZTYtOGY4OC0zNDM2M2JjN2M0YzAiOnsiY3JlYXRlIjo2MDAwMDAwMDAwMDAsImRlbGV0ZSI6OTAwMDAwMDAwMDAwfSwic2NoZW1hX3ZlcnNpb24iOiIxIn0=",
          "dependencies": [
            "data.aws_vpc.default"
          ]
        }
      ]
    }
  ]
}
```

```
$ terraform destroy
data.aws_vpc.default: Reading...
aws_key_pair.nginx-key-pair: Refreshing state... [id=nginx-key-pair]
data.aws_ami.ubuntu2204: Reading...
data.aws_vpc.default: Read complete after 1s [id=vpc-0edbd187d65482beb]
data.aws_subnets.subnets: Reading...
aws_lb_target_group.nginx-target-grp: Refreshing state... [id=arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895]
aws_security_group.nginx-security-grp: Refreshing state... [id=sg-02bf191b967d52571]
data.aws_subnets.subnets: Read complete after 0s [id=us-east-1]
aws_lb.nginx-lb: Refreshing state... [id=arn:aws:elasticloadbalancing:us-east-1:672534531507:loadbalancer/app/nginx-lb/5139d94031f6dda2]
data.aws_ami.ubuntu2204: Read complete after 1s [id=ami-052efd3df9dad4825]
aws_instance.nginx-ec2: Refreshing state... [id=i-02400694616269e82]
aws_lb_listener.nginx-lb-listener: Refreshing state... [id=arn:aws:elasticloadbalancing:us-east-1:672534531507:listener/app/nginx-lb/5139d94031f6dda2/eab6a8eae1fc644a]
aws_lb_target_group_attachment.nginx-target-grp-attach: Refreshing state... [id=arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895-20220919181433949300000001]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # aws_instance.nginx-ec2 will be destroyed
  - resource "aws_instance" "nginx-ec2" {
      - ami                                  = "ami-052efd3df9dad4825" -> null
      - arn                                  = "arn:aws:ec2:us-east-1:672534531507:instance/i-02400694616269e82" -> null
      - associate_public_ip_address          = true -> null
      - availability_zone                    = "us-east-1d" -> null
      - cpu_core_count                       = 1 -> null
      - cpu_threads_per_core                 = 1 -> null
      - disable_api_stop                     = false -> null
      - disable_api_termination              = false -> null
      - ebs_optimized                        = false -> null
      - get_password_data                    = false -> null
      - hibernation                          = false -> null
      - id                                   = "i-02400694616269e82" -> null
      - instance_initiated_shutdown_behavior = "stop" -> null
      - instance_state                       = "running" -> null
      - instance_type                        = "t2.micro" -> null
      - ipv6_address_count                   = 0 -> null
      - ipv6_addresses                       = [] -> null
      - key_name                             = "nginx-key-pair" -> null
      - monitoring                           = false -> null
      - primary_network_interface_id         = "eni-0b12553b2273359c8" -> null
      - private_dns                          = "ip-172-31-17-49.ec2.internal" -> null
      - private_ip                           = "172.31.17.49" -> null
      - public_dns                           = "ec2-54-196-249-15.compute-1.amazonaws.com" -> null
      - public_ip                            = "54.196.249.15" -> null
      - secondary_private_ips                = [] -> null
      - security_groups                      = [
          - "nginx-security-grp",
        ] -> null
      - source_dest_check                    = true -> null
      - subnet_id                            = "subnet-09634b9cc5dac6992" -> null
      - tags                                 = {
          - "Name" = "nginx-ec2"
        } -> null
      - tags_all                             = {
          - "Name" = "nginx-ec2"
        } -> null
      - tenancy                              = "default" -> null
      - user_data                            = "cde35c9c12fcd7c118915c54d146e75810da2f46" -> null
      - user_data_replace_on_change          = false -> null
      - vpc_security_group_ids               = [
          - "sg-02bf191b967d52571",
        ] -> null

      - capacity_reservation_specification {
          - capacity_reservation_preference = "open" -> null
        }

      - credit_specification {
          - cpu_credits = "standard" -> null
        }

      - enclave_options {
          - enabled = false -> null
        }

      - maintenance_options {
          - auto_recovery = "default" -> null
        }

      - metadata_options {
          - http_endpoint               = "enabled" -> null
          - http_put_response_hop_limit = 1 -> null
          - http_tokens                 = "optional" -> null
          - instance_metadata_tags      = "disabled" -> null
        }

      - private_dns_name_options {
          - enable_resource_name_dns_a_record    = false -> null
          - enable_resource_name_dns_aaaa_record = false -> null
          - hostname_type                        = "ip-name" -> null
        }

      - root_block_device {
          - delete_on_termination = true -> null
          - device_name           = "/dev/sda1" -> null
          - encrypted             = false -> null
          - iops                  = 100 -> null
          - tags                  = {} -> null
          - throughput            = 0 -> null
          - volume_id             = "vol-0a9308bd4ffaa3fec" -> null
          - volume_size           = 8 -> null
          - volume_type           = "gp2" -> null
        }
    }

  # aws_key_pair.nginx-key-pair will be destroyed
  - resource "aws_key_pair" "nginx-key-pair" {
      - arn         = "arn:aws:ec2:us-east-1:672534531507:key-pair/nginx-key-pair" -> null
      - fingerprint = "a1tkkTgj8FYwR3caF81JMefRlpABwGFxc8miekhB54A=" -> null
      - id          = "nginx-key-pair" -> null
      - key_name    = "nginx-key-pair" -> null
      - key_pair_id = "key-0dd6714964920cfe7" -> null
      - key_type    = "ed25519" -> null
      - public_key  = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILkjJM0CixodNbOvBeFudqsLtINElv3qA0EmE26+mZzH vhosakot@VHOSAKOT-M-C3TN" -> null
      - tags        = {} -> null
      - tags_all    = {} -> null
    }

  # aws_lb.nginx-lb will be destroyed
  - resource "aws_lb" "nginx-lb" {
      - arn                        = "arn:aws:elasticloadbalancing:us-east-1:672534531507:loadbalancer/app/nginx-lb/5139d94031f6dda2" -> null
      - arn_suffix                 = "app/nginx-lb/5139d94031f6dda2" -> null
      - desync_mitigation_mode     = "defensive" -> null
      - dns_name                   = "nginx-lb-473866313.us-east-1.elb.amazonaws.com" -> null
      - drop_invalid_header_fields = false -> null
      - enable_deletion_protection = false -> null
      - enable_http2               = true -> null
      - enable_waf_fail_open       = false -> null
      - id                         = "arn:aws:elasticloadbalancing:us-east-1:672534531507:loadbalancer/app/nginx-lb/5139d94031f6dda2" -> null
      - idle_timeout               = 60 -> null
      - internal                   = false -> null
      - ip_address_type            = "ipv4" -> null
      - load_balancer_type         = "application" -> null
      - name                       = "nginx-lb" -> null
      - preserve_host_header       = false -> null
      - security_groups            = [
          - "sg-02bf191b967d52571",
        ] -> null
      - subnets                    = [
          - "subnet-092224c1441f71de6",
          - "subnet-09634b9cc5dac6992",
          - "subnet-0a603f428ebf3de12",
          - "subnet-0c376d73ba74a2ed3",
          - "subnet-0e191afc433f80918",
          - "subnet-0e1e5995fe42c90a4",
        ] -> null
      - tags                       = {} -> null
      - tags_all                   = {} -> null
      - vpc_id                     = "vpc-0edbd187d65482beb" -> null
      - zone_id                    = "Z35SXDOTRQ7X7K" -> null

      - access_logs {
          - enabled = false -> null
        }

      - subnet_mapping {
          - subnet_id = "subnet-092224c1441f71de6" -> null
        }
      - subnet_mapping {
          - subnet_id = "subnet-09634b9cc5dac6992" -> null
        }
      - subnet_mapping {
          - subnet_id = "subnet-0a603f428ebf3de12" -> null
        }
      - subnet_mapping {
          - subnet_id = "subnet-0c376d73ba74a2ed3" -> null
        }
      - subnet_mapping {
          - subnet_id = "subnet-0e191afc433f80918" -> null
        }
      - subnet_mapping {
          - subnet_id = "subnet-0e1e5995fe42c90a4" -> null
        }
    }

  # aws_lb_listener.nginx-lb-listener will be destroyed
  - resource "aws_lb_listener" "nginx-lb-listener" {
      - arn               = "arn:aws:elasticloadbalancing:us-east-1:672534531507:listener/app/nginx-lb/5139d94031f6dda2/eab6a8eae1fc644a" -> null
      - id                = "arn:aws:elasticloadbalancing:us-east-1:672534531507:listener/app/nginx-lb/5139d94031f6dda2/eab6a8eae1fc644a" -> null
      - load_balancer_arn = "arn:aws:elasticloadbalancing:us-east-1:672534531507:loadbalancer/app/nginx-lb/5139d94031f6dda2" -> null
      - port              = 80 -> null
      - protocol          = "HTTP" -> null
      - tags              = {} -> null
      - tags_all          = {} -> null

      - default_action {
          - order            = 1 -> null
          - target_group_arn = "arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895" -> null
          - type             = "forward" -> null
        }
    }

  # aws_lb_target_group.nginx-target-grp will be destroyed
  - resource "aws_lb_target_group" "nginx-target-grp" {
      - arn                                = "arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895" -> null
      - arn_suffix                         = "targetgroup/nginx-target-grp/eaa304643ab02895" -> null
      - connection_termination             = false -> null
      - deregistration_delay               = "300" -> null
      - id                                 = "arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895" -> null
      - lambda_multi_value_headers_enabled = false -> null
      - load_balancing_algorithm_type      = "round_robin" -> null
      - name                               = "nginx-target-grp" -> null
      - port                               = 80 -> null
      - protocol                           = "HTTP" -> null
      - protocol_version                   = "HTTP1" -> null
      - proxy_protocol_v2                  = false -> null
      - slow_start                         = 0 -> null
      - tags                               = {} -> null
      - tags_all                           = {} -> null
      - target_type                        = "instance" -> null
      - vpc_id                             = "vpc-0edbd187d65482beb" -> null

      - health_check {
          - enabled             = true -> null
          - healthy_threshold   = 5 -> null
          - interval            = 30 -> null
          - matcher             = "200" -> null
          - path                = "/" -> null
          - port                = "traffic-port" -> null
          - protocol            = "HTTP" -> null
          - timeout             = 5 -> null
          - unhealthy_threshold = 2 -> null
        }

      - stickiness {
          - cookie_duration = 86400 -> null
          - enabled         = false -> null
          - type            = "lb_cookie" -> null
        }
    }

  # aws_lb_target_group_attachment.nginx-target-grp-attach will be destroyed
  - resource "aws_lb_target_group_attachment" "nginx-target-grp-attach" {
      - id               = "arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895-20220919181433949300000001" -> null
      - port             = 80 -> null
      - target_group_arn = "arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895" -> null
      - target_id        = "i-02400694616269e82" -> null
    }

  # aws_security_group.nginx-security-grp will be destroyed
  - resource "aws_security_group" "nginx-security-grp" {
      - arn                    = "arn:aws:ec2:us-east-1:672534531507:security-group/sg-02bf191b967d52571" -> null
      - description            = "Security group for Nginx web server" -> null
      - egress                 = [
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = ""
              - from_port        = 0
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "-1"
              - security_groups  = []
              - self             = false
              - to_port          = 0
            },
        ] -> null
      - id                     = "sg-02bf191b967d52571" -> null
      - ingress                = [
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = ""
              - from_port        = 22
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 22
            },
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = ""
              - from_port        = 80
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 80
            },
        ] -> null
      - name                   = "nginx-security-grp" -> null
      - owner_id               = "672534531507" -> null
      - revoke_rules_on_delete = false -> null
      - tags                   = {
          - "Name" = "nginx-security-grp"
        } -> null
      - tags_all               = {
          - "Name" = "nginx-security-grp"
        } -> null
      - vpc_id                 = "vpc-0edbd187d65482beb" -> null
    }

Plan: 0 to add, 0 to change, 7 to destroy.

Changes to Outputs:
  - ec2_instance_public_ip = "54.196.249.15" -> null
  - lb_public_dns          = "nginx-lb-473866313.us-east-1.elb.amazonaws.com" -> null

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

aws_key_pair.nginx-key-pair: Destroying... [id=nginx-key-pair]
aws_lb_target_group_attachment.nginx-target-grp-attach: Destroying... [id=arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895-20220919181433949300000001]
aws_lb_listener.nginx-lb-listener: Destroying... [id=arn:aws:elasticloadbalancing:us-east-1:672534531507:listener/app/nginx-lb/5139d94031f6dda2/eab6a8eae1fc644a]
aws_key_pair.nginx-key-pair: Destruction complete after 0s
aws_lb_target_group_attachment.nginx-target-grp-attach: Destruction complete after 0s
aws_instance.nginx-ec2: Destroying... [id=i-02400694616269e82]
aws_lb_listener.nginx-lb-listener: Destruction complete after 0s
aws_lb_target_group.nginx-target-grp: Destroying... [id=arn:aws:elasticloadbalancing:us-east-1:672534531507:targetgroup/nginx-target-grp/eaa304643ab02895]
aws_lb.nginx-lb: Destroying... [id=arn:aws:elasticloadbalancing:us-east-1:672534531507:loadbalancer/app/nginx-lb/5139d94031f6dda2]
aws_lb_target_group.nginx-target-grp: Destruction complete after 0s
aws_lb.nginx-lb: Destruction complete after 2s
aws_security_group.nginx-security-grp: Destroying... [id=sg-02bf191b967d52571]
aws_instance.nginx-ec2: Still destroying... [id=i-02400694616269e82, 10s elapsed]
aws_security_group.nginx-security-grp: Still destroying... [id=sg-02bf191b967d52571, 10s elapsed]
aws_instance.nginx-ec2: Still destroying... [id=i-02400694616269e82, 20s elapsed]
aws_security_group.nginx-security-grp: Still destroying... [id=sg-02bf191b967d52571, 20s elapsed]
aws_instance.nginx-ec2: Still destroying... [id=i-02400694616269e82, 30s elapsed]
aws_instance.nginx-ec2: Destruction complete after 31s
aws_security_group.nginx-security-grp: Still destroying... [id=sg-02bf191b967d52571, 30s elapsed]
aws_security_group.nginx-security-grp: Destruction complete after 30s

Destroy complete! Resources: 7 destroyed.
```
