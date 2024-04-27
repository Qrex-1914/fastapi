from fastapi import APIRouter, Depends, HTTPException
from .strategy_jhon_hernandez_taller import Strategy,Suma,Resta,Multiplicacion,Division,Contexto
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

