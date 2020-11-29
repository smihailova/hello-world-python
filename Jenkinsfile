pipeline {
  agent { docker { image 'python:3-alpine' } }
  stages {
    stage('Build') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
          sh 'pip install -r requirements.txt --user'
          sh 'ls -l'
        }
      }
    }
    stage('Test') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
          sh 'python test_app.py'
        }
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
                  sourceFiles: "./*",
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