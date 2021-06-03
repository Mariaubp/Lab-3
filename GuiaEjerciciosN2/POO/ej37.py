
class Dato:
    def __init__(self):
        self.valor1=int(input("Ingrese primer valor: "))
        self.valor2=int(input("Ingrese segundo valor: "))
        
 
    def sumar(self):
        self.suma=self.valor1 + self.valor2
        print("La suma de los valores es: ",self.suma)

    def restar(self):
        self.resta=self.valor1 - self.valor2
        print("La resta de los valores es: ",self.resta)    
 
    # declaramos el metodo mostrar
    def mostrar(self):
        print("Valor 1: ",self.valor1)
        print("Valor 2: ",self.valor2)
 

class Suma(Dato):
    def __init__(self):
        # llamamos al metodo init de la clase padre
        # utilizamos la funcion super() para hacer referencia al padre
        super().__init__()
        super().mostrar()
        super().sumar()
 
class Resta(Dato):
    def __init__(self):
        # llamamos al metodo init de la clase padre
        # utilizamos la funcion super() para hacer referencia al padre
        super().__init__()
        super().mostrar()
        super().restar()
 

 
print("PRIMERA OPERACION (suma)")
operacion1=Suma()
print("\nSEGUNDA OPERACION (resta)")
operacion2=Resta()


        