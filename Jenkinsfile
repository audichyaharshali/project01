pipeline {
    agent any

    environment {
        IMAGE_NAME = "harshitadocker01/hello"
    }

    stages {
        stage("git-checkout") {
            steps {
                checkout scm
            }
        }

        stage("image-build") {
            steps {
                script {
                    env.IMAGE_TAG = new Date().format("yyyy-MM-dd-HH-mmss")
                    env.FULL_IMAGE = "${env.IMAGE_NAME}:${env.IMAGE_TAG}"
                }

                sh 'docker build -t "$FULL_IMAGE" .'
            }
        }

        stage("docker login") {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'docker_cred',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    sh '''
                        set +x
                        echo "$DOCKER_PASSWORD" | docker login \
                            -u "$DOCKER_USERNAME" --password-stdin
                    '''
                }
            }
        }

        stage("docker push") {
            steps {
                sh 'docker push "$FULL_IMAGE"'
            }
        }
    }
}