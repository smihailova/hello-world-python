pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('Checkout') 
    {
        checkout scm
    }
    stage('Build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps {
        sh 'python test_app.py'
      }   
    }
  }
}