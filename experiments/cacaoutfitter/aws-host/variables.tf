variable "account_id" {
  type = string
  validation {
    condition     = can(regex("^[0-9]{12}$", var.account_id))
    error_message = "Select a twelve-digit AWS account ID."
  }
}
variable "course" {
  type = string
  validation {
    condition     = can(regex("^[a-z][a-z0-9-]{0,31}$", var.course))
    error_message = "Use the Waypoint course instance name."
  }
}
variable "region" { type = string }
variable "image" { type = string }
variable "flavor" { type = string }
variable "subnet_id" { type = string }
variable "security_group_id" { type = string }
variable "home_volume_id" { type = string }
