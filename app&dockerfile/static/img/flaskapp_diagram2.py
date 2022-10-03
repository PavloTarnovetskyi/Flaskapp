from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.generic.os import Ubuntu
from diagrams.onprem.iac import Ansible, Terraform
from diagrams.digitalocean.compute import Docker
from diagrams.onprem.client import Users

graph_attr = {
    "fontsize": "35",
    "bgcolor": "beige",
    "splines":"splines",
    "fontsize":"30"
}

with Diagram('Flaskapp_diagram: 2 step "Set up an environment on remote host"', show=True, graph_attr=graph_attr):
    
    user = Users("Users", fontsize="20")
    dockerhub = Custom("", "./png/dockerhub.png")        
      
    with Cluster("Localhost"):

        ansible = Ansible("Ansible", fontsize="20")           
        terraform =Terraform(" ", fontsize="20")
                    
    with Cluster("AWS EC2  Ubuntu 20.04 instance "):
       
        ubuntu = Ubuntu("", fontsize="20")  
        docker_2 = Docker("Docker", fontsize="20")
        app = Custom("", "./png/app.png")
        node_exporter = Custom ("", "./png/node-exporter.png")
        
 
    terraform >>Edge(label="1. create infrastructure on AWS")>>ubuntu
    ansible >> Edge(label="2. set up remote EC2 instance; install & run commands")>>docker_2
    docker_2 >> Edge(label="3. pull image")<<dockerhub
    docker_2>> Edge(label="4. run docker container with app")>>app
    docker_2>> Edge(label="4a. run docker container with node exporter")>>node_exporter
    user >> Edge(label="5. access app  http:<serverIP:5000>")>>app        
  