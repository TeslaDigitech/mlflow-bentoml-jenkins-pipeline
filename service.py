import json
import numpy as np
import bentoml  # Import BentoML library for creating, serving, and deploying machine learning models
import pandas as pd
import pydantic  # Import Pydantic library for data validation and parsing
from bentoml.io import JSON, PandasSeries, PandasDataFrame

# Load the latest version of the 'diabetes_pred_elastic' model, and create a runner for it
runner = bentoml.sklearn.get('diabetes_pred_elastic:latest').to_runner()

# Create a BentoML service with the loaded model
svc = bentoml.Service("diabetes_pred_elastic", runners=[runner])

# Define the API route and input/output types for the prediction endpoint
@svc.api(
    input=PandasDataFrame(),  # API input is a Pandas DataFrame
    output=JSON(),  # API output is a JSON object
    route='v1/predict/'  # API route path
)
def predict(dia_df: pd.DataFrame) -> json:
    # Rename the columns of the input DataFrame to match the expected column names
    dia_df.columns = ['age', 'sex', 'bmi',
                      'bp', 's1', 's2', 's3', 's4', 's5', 's6']
    
    # Perform the prediction using the model runner
    pred = runner.run(dia_df.astype(float))

    # Return the prediction as a JSON object
    return {'pred': pred}
