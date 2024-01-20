num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
if num1 > num2 :
    num1, num2 = num2,num1 
    
suma = sum(range(num1 +1,num2))

print(f"la suma de los numeros entre {num1} y {num2} es: {suma}")