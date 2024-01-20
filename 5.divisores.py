num =(int(input("ingrese un numero: ")))
tabla = []
for i in range(num):
    if num%(num-i)== 0:
        tabla.append(num-i)
tabla.sort()
def conversion(x):
    return str(x)
txt= ""
listan = []
for i in range(len(tabla)):
    listan = list(map(conversion,tabla))
    txt=txt+listan[i]+" "
    
print(txt)