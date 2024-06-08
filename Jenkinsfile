pipeline {
    agent any

    environment {
        //DOCKER_IMAGE = "tulakhordia/worldofgames" // Replace with your DockerHub repository
        //DOCKER_TAG = "latest"
        DOCKERHUB_CREDENTIALS = 'docker_tulak_id' // Jenkins credential ID for DockerHub
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Detect package manager and install dependencies accordingly
                    sh '''
                        if command -v apt-get > /dev/null; then
                            echo "Using apt-get for installation"
                            apt-get update
                            apt-get install -y docker.io
                            usermod -aG docker jenkins
                            apt-get install -y python3 python3-pip
                        elif command -v yum > /dev/null; then
                            echo "Using yum for installation"
                            yum update -y
                            yum install -y docker
                            usermod -aG docker jenkins
                            yum install -y python3
                            yum install -y python3-pip
                        elif command -v dnf > /dev/null; then
                            echo "Using dnf for installation"
                            dnf update -y
                            dnf install -y docker
                            usermod -aG docker jenkins
                            dnf install -y python3 python3-pip
                        else
                            echo "No supported package manager found!"
                            exit 1
                        fi

                        # Install Docker Compose
                        curl -L "https://github.com/docker/compose/releases/download/v2.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
                        chmod +x /usr/local/bin/docker-compose

                        # Start Docker service
                        sudo systemctl start docker
                        sudo systemctl enable docker
                    '''
                }
            }
        }
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