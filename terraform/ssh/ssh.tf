variable "ssh" {
  type = string
}


resource "aws_key_pair" "ssh-key" {
  key_name   = "aws-key"
  public_key = file("~/.ssh/aws-key.pub")
   tags = {
    Name = var.ssh
  }
}