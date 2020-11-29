pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'ls -l'
        sh 'python -m pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps {
        sh 'python test_app.py'
      }   
    }
  }
}