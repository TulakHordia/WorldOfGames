pipeline {
     agent { label 'node01' }

    environment {
        //DOCKER_IMAGE = "tulakhordia/worldofgames" // Replace with your DockerHub repository
        //DOCKER_TAG = "latest"
        DOCKERHUB_CREDENTIALS = 'docker_tulak_id' // Jenkins credential ID for DockerHub
        DOCKER_COMPOSE = "/opt/homebrew/bin/docker-compose"
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
                        sh '${DOCKER_COMPOSE} build'
                        sh '${DOCKER_COMPOSE} push'
                    }
                }
            }
        }

        stage('Run with Docker Compose') {
            steps {
                script {
                    // Run docker-compose up to start both app and flask
                    sh '${DOCKER_COMPOSE} up -d'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Install Python dependencies and run e2e.py tests
                    sh '''
                        pip install selenium
                        pip install webdriver_manager
                        python3 tests/e2e.py
                    '''
                }
            }
        }

        stage('Teardown') {
            steps {
                script {
                    // Stop and remove all containers started by docker-compose
                    sh '${DOCKER_COMPOSE} down'
                }
            }
        }
    }
}