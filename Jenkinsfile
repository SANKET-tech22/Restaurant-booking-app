pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/SANKET-tech22/Restaurant-booking-app.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Deploy Containers') {
            steps {
                sh 'docker compose down || true'
                sh 'docker compose up -d'
            }
        }

    }
}
