pipeline{
    agent any

    stages{
        stage('Clone'){
            steps{
                checkout scm
            }
        }

        stage('Docker Build Image'){
            steps{
                sh 'docker build -t aws-devops-project:latest .'
            }
        }

        stage('Verify Docker Image') {
            steps {
                sh 'docker images aws-devops-project'
            }
        }
    }
}
