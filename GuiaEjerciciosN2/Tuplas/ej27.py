texto = input("Ingrese una palabra: ").lower()
rever = texto[::-1]
if texto == rever:
    print("La palabra ingresada si es capicua!!")
else:
    print("La palabra ingresada no es capicua!!")