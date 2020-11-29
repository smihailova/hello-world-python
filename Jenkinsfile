pipeline {
  agent { docker { image 'python:3-alpine' } }
  stages {
    stage('Build') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
          sh 'pip install -r requirements.txt --user'
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
      script {
        sshPublisher(
          continueOnError: false, failOnError: true,
          publishers: [
            configName: "${env.SSH_CONFIG_NAME}",
            verbose: true,
            transfers: [
              sshTransfer(
                sourceFiles: "webapp/target/*",
                removePrefix: "webapp/target",
                remoteDirectory: "//opt//docker",
                execCommand: '''
                  ansible-playbook -i /opt/docker/hosts /opt/docker/create-simple-devops-image.yml --limit localhost;
                  ansible-playbook -i /opt/docker/hosts /opt/docker/create-simple-devops-project.yml --limit 34.211.184.150;
                '''
              )
            ]
          ]
        )
      }
    }
  }
}