from fastapi import FastAPI
from model import predict

app = FastAPI()

@app.post("/predict")
def run_model(data: list[float]):
    y = predict(data)
    return {"prediction": y}
