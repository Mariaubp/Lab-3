
paises=[]
habitantes=[]


def cargar(paises, habitantes):
	for x in range(5):
		nom=input("Ingrese el nombre del pais:")
		paises.append(nom)
		habit= int(input("Ingrese la cantidad de habitantes:"))
		habitantes.append([habit])


def mostrar(paises, habitantes):
	print("Listado de paises y sus habitantes")
	for x in range(5):
		print(paises[x], habitantes[x][0])


def mayor(paises, habitantes):
	posmayor=0
	mayor= habitantes[0]
	for x in range(1,5):
		if habitantes[x]>mayor:
			mayor=habitantes[x]
			posmayor=x
	print("Pais con Mayor cant de habitantes")
	print(paises[posmayor])
	print("con una cantidad de ", mayor, "habitantes ")		


def convertir(paises, habitantes):
	#convierto las listas a tuplas
	print("Convertidas las listas en tuplas")
	tuplaPaises= tuple(paises)
	print(type(tuplaPaises))
	tuplaHabitantes=tuple(habitantes)
	print(type(tuplaHabitantes))

cargar(paises, habitantes)
mostrar(paises, habitantes)
mayor(paises, habitantes)
convertir(paises, habitantes)