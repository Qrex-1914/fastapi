from fastapi import APIRouter, Depends, HTTPException
from .strategy import Strategy,Suma,Resta,Multiplicacion,Division,Contexto
from enum import Enum

class Operacion(Enum):
    SUMA = "Suma"
    RESTA = "Resta"
    MULTIPLICACION = "Multiplicacion"
    DIVISION = "Division"

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

@router.get("/suma")
def suma(num1: int, num2: int, Contexto: Strategy = Depends(get_strategy)) -> dict:
    return Contexto.ejecutar_operacion(num1=num1, num2=num2)

@router.get("/resta")

@router.get("/multiplicacion")

@router.get("/division")