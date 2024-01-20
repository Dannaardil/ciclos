
import math

num1 = int(input("ingrese el numero de potencias:"))

for potencia in  range(num1 +1):
    resultado = math.pow(potencia,2)
    
print(f"{potencia}^2 = {resultado}")
    