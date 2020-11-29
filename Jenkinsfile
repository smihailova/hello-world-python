pipeline {
  agent { docker { image 'python:3.7.2' } }
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
      steps {
        sh '''
          ansible-playbook -i /opt/docker/hosts /opt/docker/create-simple-devops-image.yml --limit localhost;
          ansible-playbook -i /opt/docker/hosts /opt/docker/create-simple-devops-project.yml --limit 34.211.184.150 ;
        '''
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