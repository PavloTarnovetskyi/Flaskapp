variable "ingress" {
  type = list(number)
  default = [22, 5000, 9100]
}

output "sg_flask" {
  value = aws_security_group.flask.name
}

resource "aws_security_group" "flask" {
  name        = "flask"
  description = "Security policies for ubuntu instance"
      dynamic ingress {
        iterator = port
        for_each = var.ingress
        content {
            from_port        = port.value
            to_port          = port.value
            protocol         = "tcp"
            cidr_blocks      = ["0.0.0.0/0"]
        }
   }

    egress {
        from_port        = 0
        to_port          = 0
        protocol         = "-1"
        cidr_blocks      = ["0.0.0.0/0"]
        ipv6_cidr_blocks = ["::/0"]
  }
}
