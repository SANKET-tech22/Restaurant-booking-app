pipeline {
    agent any

    stages {

        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Load .env from Jenkins Credentials') {
            steps {
                withCredentials([file(credentialsId: 'env-file', variable: 'ENVFILE')]) {
                    sh '''
                        cp $ENVFILE $WORKSPACE/.env
                        echo ".env loaded successfully"
                        ls -la $WORKSPACE
                    '''
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Cleanup Old Containers') {
            steps {
                sh '''
                    docker-compose down || true
                '''
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Verify Containers') {
            steps {
                sh 'docker ps'
            }
        }
    }
}
