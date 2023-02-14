import mlflow
import bentoml
from mlflow import MlflowClient
from pprint import pprint
import os


os.environ['MLFLOW_S3_ENDPOINT_URL'] = "http://localhost:9000"
mlflow.set_tracking_uri("http://localhost:5000")
all_experiments = [exp.experiment_id for exp in mlflow.search_experiments()]
df = mlflow.search_runs(experiment_ids=all_experiments,order_by=["metrics.rmse ASC"])
run_id = df.loc[0]['run_id']
print(run_id)

#artifact_path = f"mlartifacts/0/{run_id}/artifacts/model"
model_uri = f"S3://mlflow/0/{run_id}/artifacts/model"
model = mlflow.sklearn.load_model(artifact_path)
print("Printing model uri")
print(artifact_path)
print("Printing model")

try :
    if bentoml.models.get(f"diabetes_pred_elastic:{run_id}"):
        print("Model already exist")
    else:
        print("Saving the model")
        bentoml.sklearn.save_model(f"diabetes_pred_elastic:{run_id}", model)
        
except:
    print("except is executing...")
    bentoml.sklearn.save_model(f"diabetes_pred_elastic:{run_id}", model)
