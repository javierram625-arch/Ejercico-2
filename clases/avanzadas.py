import math

class Avanzadas:
    def __init__(self):

        self.num1 = 0
        self.num2 = 0


    def leerNumeros(self):
        try:
            self.num1 = float(input("Ingresa el primer número: "))
            self.num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Solo se permiten números.")
            self.leerNumeros()

    def elevarPotencia(self):
        resultado = self.num1 ** self.num2
        print(f"{self.num1} elevado a la potencia {self.num2} es: {resultado}")
        return resultado
        
        pass
    

def raiz_cuadrada(num):
    if num < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return math.sqrt(num)




