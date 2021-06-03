diccionario = {}
print("Ejemplo house:casa,big:grande,dog:perro")
palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in palabras.split(','):
    clave, valor = i.split(':')
    diccionario[clave] = valor
frase = input('Ingrese una palabra en ingles: ')
print("Palabra Traducida")
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')

        