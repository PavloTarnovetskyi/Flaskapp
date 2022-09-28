terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}
provider "aws" {
  region = "eu-north-1"
}

module "ec2ubuntu" {
  source = "./ec2"
  ec2ubuntu = "terraform_ubuntu"
}

module "vpc" {
  source = "./vpc"
    vpc = "main"
}

module "ssh" {
  source = "./ssh"
  ssh = "ssh-key"
}