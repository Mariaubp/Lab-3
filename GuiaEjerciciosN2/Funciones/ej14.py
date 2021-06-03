
def perimetro(lado):
	perimetro=lado * 4
	return perimetro


lado= int(input("Ingrese el lado del cuadrado: "))

#almacena el resultado
perimetroCalculado= perimetro(lado)

respuesta= int(input("Desea calcular el perimetro del cuadrado? (1=si-2=no):  "))
if respuesta==1:
	print("El perimetro del cuadrado es: " , perimetroCalculado)
else:
	print(" ")	

