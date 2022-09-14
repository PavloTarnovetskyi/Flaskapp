pipeline {

    agent any

    tools {
        dockerTool 'docker'
    }
    
    environment{
        dockerImage = ''
        registryCredential   = 'dockerhub-creds'
        registry = "pavlotarnovetskyi/flaskapp_jenkins"
    }
    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }
        stage('Cloning our Git '){
            steps{
                git 'https://github.com/PavloTarnovetskyi/Flaskapp.git'
            }
        }
        stage('Build & push docker image') {
            steps {   
                dir('./app&dockerfile'){ 
                    script{
                        dockerImage = docker.build registry
                        docker.withRegistry('', registryCredential) {                    
                        dockerImage.push()
                        }                            
                    }
                }
            }            
        }
        
        stage('Cleaning up') {
            steps { 
                sh "docker rmi $registry"
            }
        } 

        stage('Create EC2 ubuntu instance on AWS with terraform'){
            steps{              
                   sh """
                    terraform init
                    terraform apply -auto-approve                    
                    """
                }
            
        }
        stage('Ansible connect and deploy Flaskapp'){
            steps{
                dir('./ansible'){
                    retry(10) {
                         sh """
                        ansible-playbook playbook.yml                  
                        """
                    }    
                }
            }
        }
    
    }
}
