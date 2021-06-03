'''
--------------------------------------------------------------------------------------
Ejemplo programa usando libreria Matplotlib, muestra una serie de estudiantes,
cada uno cuenta con una cantidad de examenes aprobados de 50 que son en total
y a eso se le calcula un promedio de cuandos parciales han aprovado.
Primero se muestra un grafico de Linea que refleja la cantidad de aprobados y 
el alumno correspondiente.
Segundo se muestra un grafico de Barras que refleja el promedio de examenes 
aprovados con el alumno correspondiente.
--------------------------------------------------------------------------------------

'''

#plt es la forma mas comun de importar matplotlib
#importo matplotlib
import matplotlib.pyplot as plt

#listas con los datos de los estudiantes
nombreEstudiantes= ["Flor", "Coti", "Tomas", "Nahuel", "Martin", "Axel", "Juan", "Luis"]
#cantidad de parciales aprobados de 50 examenes
notasEstudiantes= [35, 50, 20, 45, 25, 40, 25, 40]
#porcentaje
porcentajeNotas= [35*100/50, 50*100/50, 20*100/50, 45*100/50, 25*100/50, 40*100/50, 25*100/50, 40*100/50]



def graficoDeLineaEstudiantesNotas():
    

    img= plt.imread('descarga.png')
    fig, ax=plt.subplots()

    #coordenandas izq-der-abajo-arriba
    ext=[0,100,0,800]
    ax.imshow(img, extent=ext)

    plt.plot(nombreEstudiantes, notasEstudiantes, color='black', linestyle= 'dashed', linewidth=2, marker='*', markersize=10, markerfacecolor='yellow', markeredgecolor='orange')

    #creo un diccionario con las propiedades de la fuente
    fuente1={'family':'monospace', 'style':'italic', 'weight':'bold', 'color': 'black', 'size':12}
    plt.title('Grafico de Notas de Estudiantes', fontdict=fuente1)

    fuente2={'family':'monospace', 'style':'italic', 'weight':'bold', 'color': 'red'}
    plt.xlabel('Nombre del Estudiante', fontdict=fuente2)
    plt.ylabel('Nota del Estudiante', fontdict=fuente2)
    plt.xlim(xmin=0, xmax=8)
    plt.ylim(ymin=1, ymax=50)

    fuente3={'family':'monospace', 'style':'italic', 'weight':'bold', 'color': 'white', 'size':30}
    plt.text(6,5, 'UBP', fontdict=fuente3)
    #plt.grid(True)

    aspect= img.shape[0]/float(img.shape[1])*((ext[1]-ext[0])/(ext[3]-ext[2]))
    ax.set_aspect(aspect)
    plt.savefig("PrimerGrafico")

    plt.show()
    



def graficoBarraEstudiantesPorcentaje():
    bordes= nombreEstudiantes
    alto= porcentajeNotas
    plt.bar(bordes, alto, color=['b', 'r', 'g','m','k','c','y','pink'])

    fuente1={'family':'monospace', 'style':'italic', 'weight':'bold', 'color': 'black', 'size':12}
    plt.title("Grafico de Porcentaje de Estudiantes", fontdict=fuente1)

    fuente2={'family':'monospace', 'style':'italic', 'weight':'bold', 'color': 'red'}
    plt.xlabel("Nombre del Estudiante", fontdict=fuente2)
    plt.ylabel("Porcentaje del Estudiante", fontdict=fuente2)
    plt.savefig("SegundoGrafico")
    plt.show()


graficoDeLineaEstudiantesNotas()
graficoBarraEstudiantesPorcentaje()