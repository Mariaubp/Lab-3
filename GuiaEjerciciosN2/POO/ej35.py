class Agenda:

	def __init__(self):
		# crearemos una lista donde guardaremos los datos de nuestra agenda
		self.contactos=[]
 
	def menu(self):
		print()
		menu=[
			['Agenda Personal'],
			['1. Añadir Contacto',"anadir"],
			['2. Lista de contactos'],
			['3. Buscar contacto'],
			['4. Editar contacto'],
			['5. Cerrar agenda']
		]
 
		for x in range(6):
			print(menu[x][0])
 
		opcion=int(input("Introduzca la opción deseada: "))
		if opcion==1:
			self.anadir()
		elif opcion==2:
			self.lista()
		elif opcion==3:
			self.buscar()
		elif opcion==4:
			self.editar()
		elif opcion==5:
			print("Saliendo de la agenda ...")
			exit()
 
		self.menu()
 
 
	def anadir(self):
		print("---------------------")
		print("Añadir nuevo contacto")
		print("---------------------")
		nom=input("Introduzca el nombre: ")
		telf=int(input("Introduzca el teléfono: "))
		email=input("Introduzca el email: ")
		self.contactos.append({'nombre':nom,'telf':telf,'email':email})
		
 
	def lista(self):
		print("------------------")
		print("Lista de contactos")
		print("------------------")
		if len(self.contactos) == 0:
			print("No hay ningún contacto en la agenda")
		else:
			for x in range(len(self.contactos)):
				print(self.contactos[x]['nombre'])
		
 
	# función para buscar un contacto a través del nombre
	def buscar(self):
		print("---------------------")
		print("Buscador de contactos")
		print("---------------------")
		nom=input("Introduzca el nombre del contacto: ")
		for x in range(len(self.contactos)):
			if nom == self.contactos[x]['nombre']:
				print("Datos del contacto")
				print("Nombre: ",self.contactos[x]['nombre'])
				print("Teléfono: ",self.contactos[x]['telf'])
				print("E-mail: ",self.contactos[x]['email'])
				return x
		
	def editar(self):
		print("---------------")
		print("Editar contacto")
		print("---------------")
		data=self.buscar()
		condition=False
		while condition==False:
			print("Selecciona que quieres editar: ")
			print("1. Teléfono")
			print("2. E-mail")
			print("3. Volver")
			option=int(input("Introduzca la opción deseada: "))
			if option==1:
				telf=input("Introduzca el nuevo teléfono: ")
				self.contactos[data]['telf']=telf
			elif option==2:
				email=input("Introduzca el nuevo email: ")
				self.contactos[data]['email']=email
			elif option==3:
				condition=True


agenda=Agenda()
agenda.menu()