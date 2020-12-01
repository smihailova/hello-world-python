pipeline {
  agent { docker { image 'python:3-alpine' } }
  environment {
    HOME="${env.WORKSPACE}"
  }
  stages {
    stage('Build') {
      steps {
        sh 'pip install -r src/requirements.txt'
      }
    }
    stage('Test') {
      steps {
        sh 'python -m pytest'
        // sh 'python -m coverage run -m pytest && python -m coverage html'
        // sh 'python -m pytest --junit-xml=test_results.xml || true'
        // sh 'ls -l'
        // junit keepLongStdio: true, allowEmptyResults: true, testResults: 'test_results.html'
      }
      // post {
      //   always {
      //     publishHTML target: [
      //       allowMissing: false,
      //       alwaysLinkToLastBuild: false,
      //       keepAll: true,
      //       reportDir: 'htmlcov',
      //       reportFiles: 'index.html',
      //       reportName: 'Coverage Report - Unit Test'
      //     ]
      //   }
      // }
    }
    stage('Deploy') {
      steps {
        sshPublisher(
          continueOnError: false, failOnError: true,
          publishers: [
            sshPublisherDesc(
              configName: "ansible-server",
              verbose: true,
              transfers: [
                sshTransfer(
                  sourceFiles: "requirements.txt,src/**,nginx/**,conf/**,*.yml",
                  removePrefix: "",
                  remoteDirectory: "//opt//docker",
                  execCommand: '''
                    ansible-playbook -i /opt/docker/hosts /opt/docker/create-simple-devops-image.yml --limit localhost;
                    ansible-playbook -i /opt/docker/hosts /opt/docker/create-simple-devops-project.yml --limit 34.211.184.150;
                  '''
                )
              ]
            )
          ]
        )
      }
    }
  }
}