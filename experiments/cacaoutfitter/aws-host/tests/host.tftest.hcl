mock_provider "aws" {
  mock_data "aws_subnet" {
    defaults = { availability_zone = "us-west-2a", vpc_id = "vpc-11111111" }
  }
  mock_data "aws_security_group" {
    defaults = { vpc_id = "vpc-11111111" }
  }
  mock_data "aws_ebs_volume" {
    defaults = { availability_zone = "us-west-2a", encrypted = true, id = "vol-11111111" }
  }
}

variables {
  account_id        = "111111111111"
  course            = "synthetic-course"
  region            = "us-west-2"
  image             = "ami-11111111"
  flavor            = "m7i.2xlarge"
  subnet_id         = "subnet-11111111"
  security_group_id = "sg-11111111"
  home_volume_id    = "vol-11111111"
}

run "private_host_external_homes" {
  command = plan
  assert {
    condition     = !aws_instance.hub.associate_public_ip_address && aws_instance.hub.metadata_options[0].http_tokens == "required" && aws_instance.hub.root_block_device[0].encrypted
    error_message = "Require private networking, IMDSv2 and encrypted root storage."
  }
  assert {
    condition     = aws_volume_attachment.homes.volume_id == var.home_volume_id && aws_volume_attachment.homes.stop_instance_before_detaching
    error_message = "Attach the retained course disk and stop the host before detaching."
  }
}

run "wrong_zone" {
  command = plan
  override_data {
    target = data.aws_ebs_volume.homes
    values = { availability_zone = "us-west-2b", encrypted = true }
  }
  expect_failures = [aws_instance.hub]
}

run "unencrypted_homes" {
  command = plan
  override_data {
    target = data.aws_ebs_volume.homes
    values = { availability_zone = "us-west-2a", encrypted = false }
  }
  expect_failures = [aws_instance.hub]
}

run "wrong_network" {
  command = plan
  override_data {
    target = data.aws_security_group.course
    values = { vpc_id = "vpc-22222222" }
  }
  expect_failures = [aws_instance.hub]
}
