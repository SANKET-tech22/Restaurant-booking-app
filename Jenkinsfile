pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/SANKET-tech22/Restaurant-booking-app.git'
            }
        }

        stage('Load .env File') {
            steps {
                withCredentials([file(credentialsId: 'env-file', variable: 'ENVFILE')]) {
                    sh '''
                        echo "Copying .env file to workspace"
                        cp $ENVFILE .env
                        ls -la
                    '''
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '''
                    echo "Building Docker images..."
                    docker-compose -f docker-compose.yaml build
                '''
            }
        }

        stage('Stop Old Containers') {
            steps {
                sh '''
                    echo "Stopping old containers..."
                    docker-compose -f docker-compose.yaml down || true
                '''
            }
        }

        stage('Start Containers') {
            steps {
                sh '''
                    echo "Starting containers..."
                    docker-compose -f docker-compose.yaml up -d
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    echo "Checking running containers..."
                    docker ps
                '''
            }
        }
    }
}
