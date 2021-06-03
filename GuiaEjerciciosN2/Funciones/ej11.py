def bienvenida():
    print("Bienvenido a nuestro programa")
    print("Este programa calculara la suma de dos valores enteros")
    print("********************************************************")
 

def suma():
    num1=int(input("Ingrese el primer valor:"))
    num2=int(input("Ingrese el segundo valor:"))
    suma=num1+num2
    print("La suma de los valores es: ",suma)
 
 
def despedida():
    print("********************************************************")
    print("Gracias por utilizar nuestro programa")
 
 
bienvenida()
suma()
despedida()