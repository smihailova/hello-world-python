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
        sshPublisher(
          continueOnError: false, failOnError: true,
          publishers: [
            configName: "ansible-server",
            verbose: true,
            transfers: [
              sshTransfer(
                sourceFiles: "*",
                removePrefix: "",
                remoteDirectory: "//opt//docker//python",
                execCommand: '''
                  // ansible-playbook -i /opt/docker/hosts /opt/docker/create-simple-devops-image.yml --limit localhost;
                  // ansible-playbook -i /opt/docker/hosts /opt/docker/create-simple-devops-project.yml --limit 34.211.184.150;
                '''
              )
            ]
          ]
        )
      }
    }
  }
}