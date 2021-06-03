
class Alumno:
    def inicializar(self, nombre:str, nota:int):
        self.nombre=nombre
        self.nota=nota
    def imprimir(self):
        print(f'Nombre: {self.nombre}')
        print(f'Nota: {self.nota}')


    def estado(self):
        if self.nota >=4:  
            print(f'El alumno {self.nombre} esta aprobado')
        else:
            print(f'El alumno {self.nombre} esta desaprobado')      

#bloque principal
#instancio el objeto y desp le paso los parametrps

alumno1= Alumno()    
alumno1.inicializar("Juan", 8)

alumno2= Alumno()
alumno2.inicializar("Maria", 1)

alumno3= Alumno()
alumno3.inicializar("Julieta", 10)

alumno1.imprimir()
alumno2.imprimir()
alumno3.imprimir()

alumno1.estado()
alumno2.estado()
alumno3.estado()

'''
#otra forma, le paso los atributos que yo directamente quiero que tenga
#los tengo que definir cuando instacio el objeto atraves del metodo __init__

class Alumno:
    def __init__(self, nombre:str, nota:int):
        self.nombre=nombre
        self.nota=nota
    def imprimir(self):
        print(f'Nombre: {self.nombre}')
        print(f'Nota: {self.nota}')


    def estado(self):
        if self.nota >=4:  
            print(f'El alumno {self.nombre} esta aprobado')
        else:
            print(f'El alumno {self.nombre} esta desaprobado')      

#bloque principal
alumno1= Alumno("Juan", 8)    

alumno2= Alumno("Maria", 1)

alumno3= Alumno("Julieta", 10)

alumno1.imprimir()
alumno2.imprimir()
alumno3.imprimir()

alumno1.estado()
alumno2.estado()
alumno3.estado()
'''