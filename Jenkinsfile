pipeline {
     agent { label 'node01' }

    environment {
        //DOCKER_IMAGE = "tulakhordia/worldofgames" // Replace with your DockerHub repository
        //DOCKER_TAG = "latest"
        DOCKERHUB_CREDENTIALS = 'docker_tulak_id' // Jenkins credential ID for DockerHub
        DOCKER_COMPOSE = "docker compose"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/TulakHordia/WorldOfGames.git'
            }
        }
        stage('Install Docker-compose maybe') {
            steps {
                script {
                    sh '''
                        pip install --upgrade pip
                        pip install docker
                        pip install cython
                        pip install wheel setuptools cython
                        DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
                        mkdir -p $DOCKER_CONFIG/cli-plugins
                        curl -SL https://github.com/docker/compose/releases/download/v2.27.1/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
                        chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
                        docker compose version
                    '''
                }
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