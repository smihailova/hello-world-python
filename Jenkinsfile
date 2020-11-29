pipeline {
  agent {
    label 'docker' 
  }
  stages {
    stage('build') {
      agent { docker { image 'python:3.7.2' } }
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      agent { docker { image 'python:3.7.2' } }
      steps {
        sh 'python test_app.py'
      }   
    }
  }
}