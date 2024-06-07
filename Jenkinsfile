pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = "tulakhordia/worldofgames" // Replace with your DockerHub repository
        DOCKER_TAG = "latest"
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials' // Jenkins credential ID for DockerHub
    }
    
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/TulakHordia/WorldOfGames.git'
            }
        }
        
        stage('Build') {
            steps {
                script {
                    docker.build("${env.DOCKER_IMAGE}:${env.DOCKER_TAG}")
                }
            }
        }
        
        stage('Run') {
            steps {
                script {
                    // Run Docker container exposing port 8777 and mounting dummy Scores.txt
                    sh 'echo "Dummy scores data" > Scores.txt'
                    sh 'docker run -d --name worldofgames-container -p 8777:8777 -v $PWD/Scores.txt:/app/Scores.txt ${env.DOCKER_IMAGE}:${env.DOCKER_TAG}'
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    // Ensure Python and necessary dependencies are installed
                    sh '''
                        python3 --version
                        pip install -r requirements.txt
                    '''
                    
                    // Run the e2e.py script to perform Selenium tests
                    sh 'python3 e2e.py'
                }
            }
        }
        
        stage('Finalize') {
            steps {
                script {
                    // Stop and remove the Docker container
                    sh 'docker stop worldofgames-container'
                    sh 'docker rm worldofgames-container'
                    
                    // Push Docker image to DockerHub
                    docker.withRegistry('https://index.docker.io/v1/', env.DOCKERHUB_CREDENTIALS) {
                        docker.image("${env.DOCKER_IMAGE}:${env.DOCKER_TAG}").push()
                    }
                }
            }
        }
    }
    
    post {
        always {
            script {
                // Cleanup dangling Docker images
                sh 'docker system prune -f'
            }
        }
    }
}
