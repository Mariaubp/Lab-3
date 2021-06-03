
nombre=[]
edad=[]



def cargar(nombre, edad):
	for x in range(5):
		nom=input("Ingrese el nombre de la persona:")
		nombre.append(nom)
		ed= int(input("Ingrese su edad:"))
		edad.append([ed])

def mayores(nombre, edad):
	may=[18,18,18,18,18]
	print("Listado de mayores de edad")
	for x in range(0,5):
		if (edad[x]>may):
			print(nombre[x], edad[x][0])

cargar(nombre, edad)
mayores(nombre, edad)


