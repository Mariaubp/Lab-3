
def cargar():
    agenda={}
    continuar="s"
    while continuar=="s":
        fecha=input("Ingrese la fecha con formato dd/mm/YYYY: ")
        continuar2="s"
        lista=[]
        while continuar2=="s":
            hora=input("Ingrese la hora en formato hh:mm: ")
            act=input("Ingrese la descripción de la actividad: ")
            lista.append((hora,act))
            continuar2=input("Desea ingresar otra actividad para esta fecha [s/n]: ")
        agenda[fecha]=lista
        continuar=input("Ingresar otra fecha [s/n]: ")
    return agenda
 
 
def imprimir(agenda):
    print("Listado de actividades en la agenda")
    for fecha in agenda:
        print("Fecha: ",fecha)
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)
 
 
def consultar(agenda):
    fecha=input("Ingrese una fecha a consultar en formato dd/mm/YYYY: ")
    if fecha in agenda:
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)
    else:
        print("No hay actividades para la fecha seleccionada")
 
 
agenda=cargar()
imprimir(agenda)
consultar(agenda)
