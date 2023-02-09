
import json
import numpy as np
import bentoml
import pandas as pd
import pydantic
from bentoml.io import JSON, PandasSeries, PandasDataFrame


runner = bentoml.sklearn.get('diabetes_pred_elastic:latest').to_runner()
svc = bentoml.Service("diabetes_pred_elastic", runners=[runner])


@svc.api(
    input=PandasDataFrame(),
    output=JSON(),
    route='v1/predict/'
)
def predict(dia_df: pd.DataFrame) -> json:
    dia_df.columns = ['AGE', 'SEX', 'BMI',
                        'BP', 'S1', 'S2',	'S3', 'S4', 'S5', 'S6']
    pred = runner.run(dia_df.astype(float))
    return {'pred': pred}
