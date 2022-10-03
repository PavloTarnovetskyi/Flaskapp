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
        stage('Cloning our Git '){
            steps{
                slackSend channel: 'jenkins-messages', message: "The job ${env.JOB_NAME} ${env.BUILD_NUMBER} ${env.BUILD_URL} has started its work!"
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
                dir('./terraform'){            
                    sh """
                    terraform init
                    terraform apply -auto-approve -no-color                   
                        """
                }        
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

    post
    {
        always
        {
            slackSend channel: 'jenkins-messages', message: "Please find status of pipeline ${env.JOB_NAME} ${env.BUILD_NUMBER} ${env.BUILD_URL}"
        }

    }
}
