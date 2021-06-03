
class Empleado:
	# inicializamos nuestros atributos
	def __init__(self):
		self.nombre=input("Ingrese el nombre: ")
		self.sueldo=int(input("Ingrese el sueldo: "))
 
	# imprimimos los datos
	def imprimir(self):
		print("Empleado")
		print("Nombre: ",self.nombre)
		print("Sueldo: ",self.sueldo)
 
	def mayor_salario(self):
		if self.sueldo >= 3000:
			print("Debe pagar impuestos")
		else:
			print("No debe pagar impuestos")
 
 

empleado1=Empleado()

empleado1.imprimir()
empleado1.mayor_salario()
