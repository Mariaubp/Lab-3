
def mayor(nro1, nro2, nro3):
	if nro1>nro2 and nro1>nro3:
		return nro1
	elif nro1< nro2> nro3:
		return nro2
	elif nro1< nro3> nro2:
		return nro3



nro1= int(input("Ingrese el primer numero: "))
nro2= int(input("Ingrese el segundo numero: "))
nro3= int(input("Ingrese el tercer numero: "))

#almacena el resultado
mayorCalculado= mayor(nro1, nro2, nro3)

print("El mayor numero es: " , mayorCalculado)
