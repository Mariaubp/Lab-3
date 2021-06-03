
class Punto:
    def inicializar(self):
        self.x=int(input("Ingrese el valor de X: "))
        self.y=int(input("Ingrese el valor de Y: "))
 
    def imprimir(self):
        print("Los datos del Punto son:")
        print("Valor X: ",self.x)
        print("Valor Y: ",self.y)
 

    def cuadrante(self):
        if self.x>0 and self.y>0:
            print("Esta en el primer cuadrante ")
        elif self.x<0 and self.y>0:
            print("Esta en el segundo cuadrante")
        elif self.x<0 and self.y<0:
            print("Esta en el tercer cuadrante")    
        else:
            print("Esta en el tercer cuadrante")
 

 

punto1=Punto()
punto1.inicializar()
punto1.imprimir()
punto1.cuadrante()

