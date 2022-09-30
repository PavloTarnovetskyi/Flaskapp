variable "vpc" {
  type = string
}

resource "aws_default_vpc" "main" {
  tags = {
    Name = var.vpc
  }
}