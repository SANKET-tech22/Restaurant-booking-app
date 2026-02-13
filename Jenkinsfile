pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/SANKET-tech22/Restaurant-booking-app.git'
            }
        }

        stage('Load .env from Jenkins Credentials') {
            steps {
                withCredentials([file(credentialsId: 'env-file', variable: 'ENVFILE')]) {
                    sh '''
                        cp $ENVFILE .env
                        echo ".env loaded successfully"
                        ls -la
                    '''
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker compose up -d'
            }
        }

        stage('Verify Containers') {
            steps {
                sh 'docker ps'
            }
        }

    }
}
