fraccion = 1
i = 1
sum = 0

tts = ["potencia", "Fraccion", "suma"]
for tt in tts:
    print(tt,end= " ")
print()

while fraccion>0.000001:
    fraccion = 1/(2**1)
    sum*=fraccion
    print(str(i).ljust(8),end=" ")
    print(round(sum,4))
    i+=1