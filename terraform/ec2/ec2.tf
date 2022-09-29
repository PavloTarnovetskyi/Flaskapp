variable "ec2ubuntu" {
  type = string
}

resource "aws_instance" "terraform_ubuntu" {
  ami                    = "ami-092cce4a19b438926" # Ubuntu Server 20.04 LTS ami
  instance_type          = "t3.micro"
  key_name               = "aws-key"
  vpc_security_group_ids = [module.security_group.sg_flask]
  iam_instance_profile   = "${aws_iam_instance_profile.ec2_profile.name}"
  tags                   =   {
  "Name"                 = var.ec2ubuntu
  }
}

module "security_group" {
  source  = "../sg"
}

resource "aws_iam_role_policy_attachment" "AmazonSSMFullAccess" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonSSMFullAccess"
  role       = aws_iam_role.ec2_ssm_role.name
}

resource "aws_iam_role" "ec2_ssm_role"{
  name = "ec2_ssm_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      },
    ]
  })

  tags = {
    tag-key = "tag-value"
  }
}

resource "aws_iam_instance_profile" "ec2_profile" {
  name = "ec2_ssm_profile"
  role = "${aws_iam_role.ec2_ssm_role.name}"
}

output "ip" {
  value = aws_instance.terraform_ubuntu.public_ip
}


resource "local_file" "public_ip_for_deploy" {
   content = <<EOT
    [terraform_ubuntu]
    ${aws_instance.terraform_ubuntu.public_ip}  
      EOT
      filename = "../ansible/serverIP.txt"
      }