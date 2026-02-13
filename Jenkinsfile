pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/SANKET-tech22/Restaurant-booking-app.git'
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
                sh '''
                    docker compose build
                '''
            }
        }

        stage('Force Cleanup Old Containers') {
            steps {
                sh '''
                    echo "Stopping and removing old containers..."

                    docker compose down || true

                    docker stop restaurant-postgres || true
                    docker rm restaurant-postgres || true

                    docker stop restaurant-backend || true
                    docker rm restaurant-backend || true

                    docker stop restaurant-frontend || true
                    docker rm restaurant-frontend || true

                    echo "Cleanup completed."
                '''
            }
        }

        stage('Run Containers') {
            steps {
                sh '''
                    echo "Starting new containers..."
                    docker compose up -d
                '''
            }
        }

        stage('Verify Containers') {
            steps {
                sh '''
                    echo "Running containers:"
                    docker ps
                '''
            }
        }

    }
}
