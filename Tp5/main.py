import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils import paisesInfo


def main():

    
        casos_pais = {}
        
        inicioPeriodo = "2021-03-01"
        finPeriodo = "2021-03-31"

        for pais in paisesInfo():
            urlCasos = f"https://api.covid19api.com/country/{pais}/status/confirmed?from={inicioPeriodo}T00:00:00Z&to={finPeriodo}T00:00:00Z"
            response = requests.get(urlCasos)
            if response.status_code == 200 and len(response.json()) >= 2:
                casos_inicio = []
                casos_final = []
                casos_inicio_total = 0
                casos_final_total = 0

                for dato in response.json():
                    if dato["Date"] == inicioPeriodo + "T00:00:00Z":
                        casos_inicio.append(dato["Cases"])
                    if dato["Date"] == finPeriodo + "T00:00:00Z":
                        casos_final.append(dato["Cases"])
                    print(dato["Country"] + ": " + str(dato["Cases"]))
                
                for x in range(len(casos_inicio)):
                    casos_inicio_total = casos_inicio_total + casos_inicio[x]
                for y in range(len(casos_final)):
                    casos_final_total = casos_final_total + casos_final[y]

                casos_pais[pais] = casos_final_total - casos_inicio_total
                casos_pais_ordenado = sorted(casos_pais.items(), key=lambda x: x[1], reverse=True)

        
        print('\n')
        print("Paises ordenados por cantidad de casos")
        print(casos_pais_ordenado)

        paises = []
        print('\n')
        print("PODIO 3 PRIMEROS PAISES")
        
        for i in casos_pais_ordenado:
            paises.append(i[0])
            
        primerosTresPaises=paises[0:3]
        print(primerosTresPaises) 
            

        #toma el 2do elemento de la tupla, los casos
        casos = []
        for i in casos_pais_ordenado:
            casos.append(i[1])
            
        primerosTresCasos=casos[0:3]
        print(primerosTresCasos)   
       

        fig, ax =plt.subplots(1,1)
        data =  [[ primerosTresPaises[0], primerosTresCasos[0]],
                 [ primerosTresPaises[1], primerosTresCasos[1]],
                 [ primerosTresPaises[2], primerosTresCasos[2]]]

 
        column_labels=["PAISES ", "CASOS "]
        df=pd.DataFrame(data,columns=column_labels)
        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=df.values,
        colLabels=df.columns,
        rowLabels=["1er Puesto","2do Puesto","3er Puesto"],
        rowColours =["blue"] * 3,  
        colColours =["blue"] * 2,
        loc="center")

        fuente1={'family':'monospace', 'style':'italic', 'weight':'bold', 'color': 'black', 'size':13}
        plt.title ('CASOS COVID ENTRE 1 DE MARZO DEL 2021 AL 31 DE MARZO DEL 2021', fontdict=fuente1)
        plt.show()

        muertesFuncion()



        ##############################################################################################

def muertesFuncion():
        muertes_pais = {}
        
        inicioPeriodo = "2021-03-01"
        finPeriodo = "2021-03-31"

        for pais in paisesInfo():
            urlMuertes = f"https://api.covid19api.com/country/{pais}/status/deaths?from={inicioPeriodo}T00:00:00Z&to={finPeriodo}T00:00:00Z"
            response = requests.get(urlMuertes)
            if response.status_code == 200 and len(response.json()) >= 2:
                muertes_inicio = []
                muertes_final = []
                muertes_inicio_total = 0
                muertes_final_total = 0

                for dato in response.json():
                    if dato["Date"] == inicioPeriodo + "T00:00:00Z":
                        muertes_inicio.append(dato["Cases"])
                    if dato["Date"] == finPeriodo + "T00:00:00Z":
                        muertes_final.append(dato["Cases"])
                    print(dato["Country"] + ": " + str(dato["Cases"]))
                
                for x in range(len(muertes_inicio)):
                    muertes_inicio_total = muertes_inicio_total + muertes_inicio[x]
                for y in range(len(muertes_final)):
                    muertes_final_total = muertes_final_total + muertes_final[y]

                muertes_pais[pais] = muertes_final_total - muertes_inicio_total
                muertes_pais_ordenado = sorted(muertes_pais.items(), key=lambda x: x[1], reverse=True)

        
        print('\n')
        print("Paises ordenados por cantidad de casos")
        print(muertes_pais_ordenado)

        paises = []
        print('\n')
        print("PODIO 3 PRIMEROS PAISES")
        
        for i in muertes_pais_ordenado:
            paises.append(i[0])
            
        primerosTresPaises=paises[0:3]
        print(primerosTresPaises) 
            

        #toma el 2do elemento de la tupla, los casos
        muertes = []
        for i in muertes_pais_ordenado:
            muertes.append(i[1])
            
        primerosTresMuertes=muertes[0:3]
        print(primerosTresMuertes)   
       

        fig, ax =plt.subplots(1,1)
        data =  [[ primerosTresPaises[0], primerosTresMuertes[0]],
                 [ primerosTresPaises[1], primerosTresMuertes[1]],
                 [ primerosTresPaises[2], primerosTresMuertes[2]]]

 
        column_labels=["PAISES ", "MUERTES "]
        df=pd.DataFrame(data,columns=column_labels)
        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=df.values,
        colLabels=df.columns,
        rowLabels=["1er Puesto","2do Puesto","3er Puesto"],
        rowColours =["blue"] * 3,  
        colColours =["blue"] * 2,
        loc="center")

        fuente1={'family':'monospace', 'style':'italic', 'weight':'bold', 'color': 'black', 'size':13}
        plt.title ('MUERTES COVID ENTRE 1 DE MARZO DEL 2021 AL 31 DE MARZO DEL 2021', fontdict=fuente1)
        plt.show()
        





    

if __name__ == '__main__':
    main()