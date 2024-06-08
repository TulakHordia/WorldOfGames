pipeline {
    agent any

    environment {
        //DOCKER_IMAGE = "tulakhordia/worldofgames" // Replace with your DockerHub repository
        //DOCKER_TAG = "latest"
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
                    // Build and push app and flask images
                    docker.withRegistry('', DOCKERHUB_CREDENTIALS) {
                        sh 'docker-compose build'
                        sh 'docker-compose push'
                    }
                }
            }
        }

        stage('Run with Docker Compose') {
            steps {
                script {
                    // Run docker-compose up to start both app and flask
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Install Python dependencies and run e2e.py tests
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
                    // Stop and remove all containers started by docker-compose
                    sh 'docker-compose down'
                }
            }
        }
    }
}