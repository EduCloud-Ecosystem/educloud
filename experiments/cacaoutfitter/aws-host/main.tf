terraform {
  required_version = ">= 1.6"
  required_providers {
    aws = {
      source  = "registry.terraform.io/hashicorp/aws"
      version = "= 6.74.0"
    }
  }
}

provider "aws" {
  region              = var.region
  allowed_account_ids = [var.account_id]
}

data "aws_subnet" "course" {
  id = var.subnet_id
}

data "aws_security_group" "course" {
  id = var.security_group_id
}

# Retained storage belongs to the course operator across host replacements.
data "aws_ebs_volume" "homes" {
  filter {
    name   = "volume-id"
    values = [var.home_volume_id]
  }
  filter {
    name   = "tag:EduCloudCourse"
    values = [var.course]
  }
}

resource "aws_instance" "hub" {
  ami                         = var.image
  instance_type               = var.flavor
  subnet_id                   = var.subnet_id
  vpc_security_group_ids      = [var.security_group_id]
  associate_public_ip_address = false

  root_block_device {
    encrypted             = true
    volume_type           = "gp3"
    delete_on_termination = true
  }
  metadata_options {
    http_tokens                 = "required"
    http_put_response_hop_limit = 1
  }
  tags = {
    Name           = "educloud-${var.course}-hub"
    EduCloudCourse = var.course
  }
  lifecycle {
    precondition {
      condition     = data.aws_subnet.course.vpc_id == data.aws_security_group.course.vpc_id
      error_message = "The course subnet and security group must belong to the same VPC."
    }
    precondition {
      condition     = data.aws_ebs_volume.homes.encrypted && data.aws_ebs_volume.homes.availability_zone == data.aws_subnet.course.availability_zone
      error_message = "The retained course volume must be encrypted and in the host subnet's availability zone."
    }
  }
}

resource "aws_volume_attachment" "homes" {
  instance_id                    = aws_instance.hub.id
  volume_id                      = data.aws_ebs_volume.homes.id
  device_name                    = "/dev/sdf"
  stop_instance_before_detaching = true
}

# CACAO's AWS single-image recipe uses list outputs for both fields.
output "instance_uuids" {
  value = [aws_instance.hub.id]
}

output "instance_ips" {
  description = "Private address of the course host."
  value       = [aws_instance.hub.private_ip]
}
