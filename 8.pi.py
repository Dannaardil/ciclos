n = int(input("N: "))
lista = []

for i in range(n):
    estimacion = ((-1)**i)/((2*i)+1)
    lista.append(estimacion)

sumatoria = sum(lista)*4
print(sumatoria)