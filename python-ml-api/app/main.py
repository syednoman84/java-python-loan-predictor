from fastapi import FastAPI
from app.api.endpoints import predict
from app.api.endpoints import predict_lc

app = FastAPI()

app.include_router(predict.router)
app.include_router(predict_lc.router)
