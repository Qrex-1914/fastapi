from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, num1, num2):
        pass

class Suma(Strategy):
    def execute(self, num1, num2):
        return num1 + num2

class Resta(Strategy):
    def execute(self, num1, num2):
        return num1 - num2

class Multiplicacion(Strategy):
    def execute(self, num1, num2):
        return num1 * num2

class Division(Strategy):
    def execute(self, num1, num2):
        if num2 == 0:
            return 0
        else :
            return num1 / num2


#la estrategia
class Contexto:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def ejecutar_operacion(self, num1, num2):
        return self.estrategia.execute(num1, num2)

# Ejemplo de uso
if __name__ == "__main__":
    contexto = Contexto(Suma())
    resultado = contexto.ejecutar_operacion(10, 5)
    print("Resultado de la suma:", resultado)

    contexto = Contexto(Resta())
    resultado = contexto.ejecutar_operacion(10, 5)
    print("Resultado de la resta:", resultado)