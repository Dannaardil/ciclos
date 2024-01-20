numero = int(input("introduzca un numero: "))
while numero != 1:
    print(int(numero)," ")
    if numero%2==0:
        numero/2
    else:
        numero=numero*3+1
    print(1)