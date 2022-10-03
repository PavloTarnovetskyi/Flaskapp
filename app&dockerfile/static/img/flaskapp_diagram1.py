from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.vcs import Github
from diagrams.onprem.iac import Ansible, Terraform
from diagrams.digitalocean.compute import Docker
from diagrams.saas.chat import Slack
from diagrams.onprem.client import Users

graph_attr = {
    "fontsize": "35",
    "bgcolor": "beige",
    "splines":"splines",
    "fontsize":"30"
}

with Diagram('Flaskapp_diagram: 1 step "Set up an environment on localhost"', show=True, graph_attr=graph_attr):
    
    github = Github("Github repository", fontsize="20")  
    dockerhub = Custom("dockerhub", "./png/dockerhub.png")        
    devops = Custom("DevOps", "./png/devops.png")
    
    with Cluster("LocalHost"):
        jenkins = Jenkins("Jenkins", fontsize="20")
        ansible = Ansible("Ansible", fontsize="20")           
        terraform =Terraform(" ", fontsize="20")
        docker_1 = Docker("Docker", fontsize="20")
        slack = Slack("Slack")   

    jenkins >> Edge(label="send information about pipeline stage (3,5,6)")>>slack
    devops >> Edge(label="1. push code to")>>github
    github >> Edge(label="2. webhook or PollSCM")<< jenkins  
    jenkins >> Edge(label="3. build image")<<docker_1
    docker_1 >> Edge(label="4. push image")>>dockerhub
    jenkins >> Edge(label="5. start terraform plan")<<terraform 
    jenkins >> Edge(label="6. run ansible-playbook")<<ansible