pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'whoami'
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

// pipeline {
//     agent none 
//     stages {
//         stage('Build') { 
//             agent {
//                 docker {
//                     image 'python:3-alpine' 
//                 }
//             }
//             steps {
//                 sh 'python -m py_compile sources/add2vals.py sources/calc.py' 
//                 stash(name: 'compiled-results', includes: 'sources/*.py*') 
//             }
//         }
//     }
// }