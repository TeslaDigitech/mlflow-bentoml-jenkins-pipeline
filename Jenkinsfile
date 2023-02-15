pipeline{
    agent any
  
  stages {  
  stage('Setting up the mlflow'){
      
            steps{
                sh "pip install -r requirements.txt "
                sh "pip install mlflow"

            }
      
    }
    stage('Training the model ') {
            steps {
                sh "python3 train.py" 
              
            }
        } 
  
    stage('Choosing the best model') {
      
            steps {
                sh "python3 chosing_model.py"
            }
      
    }
    stage('Building the bento') {
            steps {
                sh "python3 -m bentoml build || echo 'bento already exist'"
              
            }
        } 
    stage('bento containerize') {
            steps {
                sh "python3 -m bentoml containerize -t diabetes_pred_elastic:latest diabetes_pred_elastic:latest" 
            }
        }
    stage('docker stop container') {
            steps {
                sh "docker stop diabetes_pred || true" 
            }
        }
     stage('docker start container') {
            steps {
                sh "docker run -itd --rm -p 3000:3000 --name diabetes_pred diabetes_pred_elastic:latest serve --production" 
            }
        }
    stage('docker prune images') {
            steps {
                sh "docker image prune -f" 
            }
        }
}
}
