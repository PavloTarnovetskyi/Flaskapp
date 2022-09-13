pipeline {
    agent any
    tools {
        dockerTool 'docker'
        terraform 'terraform'
    }
    environment{
        dockerHubPwd   = credentials('dockerhub_pwd')
    }
    stages {
        stage('Git clone'){
            steps{
                git url: 'https://github.com/PavloTarnovetskyi/Onboarding.git', credentialsId: 'github', branch: 'master'
            }
        }
        stage('Build docker image') {
            steps {
                dir('./Flaskapp_GitHub'){
                   sh """
                    docker build -t pavlotarnovetskyi/flaskapp_jenkins .
                    """
                }
            } 
            
        }
        stage('Push docker image to dockerhub & remove image') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub_pwd', variable: 'password_dockerhub')]){
                    sh "docker login -u pavlotarnovetskyi -p ${env.dockerHubPwd}"
                    sh '''
                        docker push pavlotarnovetskyi/flaskapp_jenkins
                        docker rmi pavlotarnovetskyi/flaskapp_jenkins
                    ''' 
                }
            
            } 
        }
        stage('Create EC2 ubuntu instance on AWS with terraform'){
            steps{
              dir('./Flaskapp_GitHub'){
                   sh """
                    terraform init
                    terraform apply -auto-approve                    
                    """
                }
            }
        }
        stage('Ansible connect and deploy Flaskapp'){
            steps{
              dir('./Flaskapp_GitHub/ansible'){
                   sh """
                     ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook playbook.yml                  
                    """
                }
            }
        }
    
    }
}
