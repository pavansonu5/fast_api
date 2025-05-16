# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

# create a app
app=FastAPI()

class diamond_inputs(BaseModel):
    carat: float
    cut: int
    color: int 
    clarity:int 
    x:float
    y:float
    z:float

@app.post("/predict")
def predict_price(data: diamond_inputs):
    input_array=np.array([[data.carat,data.cut,data.color,data.clarity,data.x,data.y,data.z]])
    result=model.predict(input_array)
    return {"predicted_price":int(result[0])}
