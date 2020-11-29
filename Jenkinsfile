pipeline {
  agent { docker { image 'python:3-alpine' } }
  environment {
    HOME="${env.WORKSPACE}"
  }
  stages {
    stage('Build') {
      steps {
        sh 'pip install -r requirements.txt --user'
        sh 'ls -l'
      }
    }
    stage('Test') {
      steps {
        sh 'python test_app.py'
      }
    }
    stage('Deploy') {
      steps {
        sh 'ls -l'
        sshPublisher(
          continueOnError: false, failOnError: true,
          publishers: [
            sshPublisherDesc(
              configName: "ansible-server",
              verbose: true,
              transfers: [
                sshTransfer(
                  sourceFiles: "requirements.txt,app.py,Dockerfile,conf/gunicorn_config.py",
                  removePrefix: "",
                  remoteDirectory: "//opt//docker",
                  execCommand: "ansible-playbook -i /opt/docker/hosts /opt/docker/create-simple-devops-image.yml --limit localhost;ansible-playbook -i /opt/docker/hosts /opt/docker/create-simple-devops-project.yml --limit 34.211.184.150 ;"
                )
              ]
            )
          ]
        )
      }
    }
  }
}