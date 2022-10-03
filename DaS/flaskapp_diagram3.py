from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.vcs import Github
from diagrams.generic.os import Ubuntu
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

with Diagram('Flaskapp_diagram: 3 step "Server monitoring"', show=True, graph_attr=graph_attr):
       
    devops = Custom("DevOps", "./png/devops.png")
    
    with Cluster("Localhost"):
          
        grafana = Custom("", "./png/grafana.png")
        prometheus = Custom("", "./png/prometheus.png")
        

                    
    with Cluster("AWS EC2  Ubuntu 20.04 instance "):
                
        ubuntu = Ubuntu("", fontsize="20")  
        node_exporter = Custom ("node exporter", "./png/node-exporter.png")

      
    prometheus >> Edge(label="1. takes metrics from EC2 instance")<<node_exporter
    prometheus >> Edge(label="2. metrics dashboarding")<<grafana
    devops >> Edge(label="3. take information about instance for monitoring")>>grafana
   