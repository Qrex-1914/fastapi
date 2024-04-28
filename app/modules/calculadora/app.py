from fastapi import APIRouter, Depends, HTTPException
from .strategy import Strategy,Suma,Resta,Multiplicacion,Division
from enum import Enum

class Operacion(Enum):
    SUMA = "suma"
    RESTA = "resta"
    MULTIPLICACION = "multiplicacion"
    DIVISION = "division"

def get_strategy(Operacion: Operacion) -> Strategy:
    if Operacion == Operacion.SUMA:
        return Suma()
    elif Operacion == Operacion.RESTA:
        return Resta()
    elif Operacion == Operacion.MULTIPLICACION:
        return Multiplicacion()
    elif Operacion == Operacion.DIVISION:
        return Division()
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")


router = APIRouter()

@router.get("/operacion")
def operacion(num1: int, num2: int, operation: Strategy = Depends(get_strategy)) -> float:
    return operation.execute(num1=num1, num2=num2)