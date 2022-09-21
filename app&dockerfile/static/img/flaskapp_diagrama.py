from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.vcs import Github
from diagrams.generic.os import Ubuntu
from diagrams.onprem.iac import Ansible, Terraform
from diagrams.digitalocean.compute import Docker

graph_attr = {
    "fontsize": "35",
    "bgcolor": "beige",
    "splines":"splines",
    "fontsize":"30"
}

with Diagram("Flaskapp_diagrama", show=True, graph_attr=graph_attr):
    
    github = Github("Github repository", fontsize="20")
    user = Custom("User", "./png/user.png")
    dockerhub = Custom("dockerhub", "./png/dockerhub.png")        
    devops = Custom("DevOps", "./png/devops.png")
    
    with Cluster("Localhost"):
        jenkins = Jenkins("Jenkins", fontsize="20")
        ansible = Ansible("Ansible", fontsize="20")           
        terraform =Terraform(" ", fontsize="20")
        docker_1 = Docker("Docker", fontsize="20")

                    
    with Cluster("AWS EC2  ubuntu 20.04 instance "):
                
        ubuntu = Ubuntu("", fontsize="20")  
        docker_2 = Docker("Docker", fontsize="20")
        app = Custom("", "./png/app.png")

    
    devops >> Edge(label="1. push code to")>>github
    github >> Edge(label="2. webhook or PollSCM")<< jenkins  
    jenkins >> Edge(label="3. build image")<<docker_1
    docker_1 >> Edge(label="4. push image")>>dockerhub
    jenkins >> Edge(label="5. start terraform plan")<<terraform 
    terraform >>Edge(label="5a. create infrastructure on AWS")>>ubuntu
    jenkins >> Edge(label="6. run ansible-playbook")<<ansible 
    ansible >> Edge(label="7. set up remote EC2 instance; install & run commands")>>docker_2
    docker_2 >> Edge(label="8. pull image")<<dockerhub
    docker_2>> Edge(label="9. run docker container with app")>>app
    user >> Edge(label="10. access app  http:<serverIP:5000>")>>app        