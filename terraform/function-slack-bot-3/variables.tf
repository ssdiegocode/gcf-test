variable "project_id" {}

variable "region" {
  default = "us-east1"
}

variable "slack_url" {
  description = "Slack webhook URL"
  type        = string
  default     = ""  # Allows local Terraform runs without needing this variable
}
