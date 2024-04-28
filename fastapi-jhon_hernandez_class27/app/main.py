import os
from typing import Union

from fastapi import FastAPI, Depends
from starlette.responses import FileResponse

from modules.routes.app import get_strategy
from modules.routes.strategy import Strategy

app = FastAPI()

current_dir = os.path.dirname(os.path.realpath(__file__))


@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/operacion")
def operacion(num1: int, num2: int, operation: Strategy = Depends(get_strategy)) -> float:
    return operation.execute(num1=num1, num2=num2)