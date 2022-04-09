pipeline {

  agent any

  environment {
    AWS_ACCESS_KEY = credentials('AWS_ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
    imagename = "rinesashkodra/cdp2:docker"
    registryCredential = 'DockerAcess'
    dockerImage = ''
    BRANCH_NAME = "${GIT_BRANCH.split("/")[1]}"
  }

stages {
  stage('Checkout git repo') {
    steps {
         script{
      if (env.BRANCH_NAME == 'main') {
        BUILD_TYPE = 'deploy'
      } else {
        BUILD_TYPE = 'test'
      }
    }
    }
  }

  
    stage('Build Image') {
      steps {
          script{
             dockerImage = docker.build imagename
          }
      }
    }  
    stage('Push Image') {
      steps {
         
          script
          {docker.withRegistry( '', registryCredential ) {
          dockerImage.push("$BUILD_NUMBER")
          dockerImage.push('latest')
              }
       
      }
    }
    }
     stage('Run Image') {
      steps {
         
         sh 'echo $AWS_ACCESS_KEY'
         sh 'docker run --rm -e AWS_ACCESS_KEY=$AWS_ACCESS_KEY  -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY  rinesashkodra/cdp2'
      }
    }
    }
   
}

