pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'docker_tulak_id' // Jenkins credential ID for DockerHub
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/TulakHordia/WorldOfGames.git'
            }
        }

        stage('Build and Push') {
            steps {
                script {
                    // Ensure Docker is running
                    sh 'docker --version'

                    // Build and push Docker images
                    docker.withRegistry('https://index.docker.io/v1/', env.DOCKERHUB_CREDENTIALS) {
                        sh 'docker-compose build'
                        sh 'docker-compose push'
                    }
                }
            }
        }

        stage('Run with Docker Compose') {
            steps {
                script {
                    // Start services with Docker Compose
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Install Python dependencies and run tests
                    sh '''
                        pip install -r requirements.txt
                        python3 e2e.py
                    '''
                }
            }
        }

        stage('Teardown') {
            steps {
                script {
                    // Stop and remove all containers
                    sh 'docker-compose down'
                }
            }
        }
    }
}
