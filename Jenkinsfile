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
                  sourceFiles: ".",
                  removePrefix: "",
                  remoteDirectory: "//opt//docker",
                  execCommand:""
                )
              ]
            )
          ]
        )
      }
    }
  }
}