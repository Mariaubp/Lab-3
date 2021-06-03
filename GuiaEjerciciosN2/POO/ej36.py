import random as R

def main():
    
    contador = 0 
  
    dado1 = R.randint (1,6)
    dado2 = R.randint (1,6)
    dado3 = R.randint (1,6)
    
    
    print ("Resultado tirada dado1: ", dado1)
    print ("Resultado tirada dado2: ", dado2)
    print ("Resultado tirada dado3: ", dado3)
 
#ompruebo si los tres dados son iguales a 6
    if dado1 == dado2 and dado1==dado3 :
        print ("Ganaste")
    else :
        print ("Perdiste")
    
main()    