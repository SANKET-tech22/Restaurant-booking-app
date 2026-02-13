pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/SANKET-tech22/Restaurant-booking-app.git'
            }
        }

        stage('Create .env file') {
            steps {
                sh '''
                cat <<EOF > .env
DATABASE_URL=postgresql://postgres:postgres@db:5432/restaurant
SECRET_KEY=mysecretkey
DEBUG=True
EOF
                '''
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

        stage('Check Running Containers') {
            steps {
                sh 'docker ps'
            }
        }

    }
}
