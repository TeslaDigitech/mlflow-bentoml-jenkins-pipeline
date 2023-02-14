pipeline{
    agent any
  
  stages {  
  stage('Setting up the mlflow'){
      
            steps{
                sh "pip3 install -r requirements.txt "
                sh "export MLFLOW_TRACKING_URI=http://localhost:5000"
                sh "export MLFLOW_S3_ENDPOINT_URL=http://localhost:9000"
                sh "export AWS_ACCESS_KEY_ID=minio"
                sh "export AWS_SECRET_ACCESS_KEY=minio123"
                
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
                sh "bentoml build || echo 'bento already exist'" 
              
            }
        } 
    stage('bento containerize') {
            steps {
                sh "bentoml containerize diabetes_pred_elastic:latest" 
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
