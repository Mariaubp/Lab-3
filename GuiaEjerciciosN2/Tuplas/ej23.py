
diccionario= {"mesa": 120, "silla": 50, "sillon": 80, "ventana": 500, "puerta":8000}



print("\nElementos del Diccionario")
for clave in diccionario:
	print(clave, ":", diccionario[clave])

print("\nElementos con precio mayor de $100 del Diccionario")
for clave in diccionario:
	if diccionario[clave]>100:
		print(clave, ":", diccionario[clave])