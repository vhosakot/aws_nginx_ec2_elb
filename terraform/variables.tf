# (Optional) VPC ID used to create Security Group and Target Group used by Load Balancer
variable "vpc_id" {
  description = "(Optional) VPC ID. Default is empty string"
  type        = string
  default     = ""
}
# (Optional) Subnet ID used to create EC2 instance
variable "subnet_id" {
  description = "(Optional) Subnet ID. Default is empty string"
  type        = string
  default     = ""
}
variable "ssh_public_key" {
  description = "SSH public key (for example in ~/.ssh/id_ed25519.pub)"
  type        = string
  default     = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILkjJM0CixodNbOvBeFudqsLtINElv3qA0EmE26+mZzH vhosakot@VHOSAKOT-M-C3TN"
}
variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}
variable "ami_image_name" {
  description = "AMI image name"
  type        = string
  default     = "*ubuntu-jammy-22.04-amd64-server-20220609*"
}
