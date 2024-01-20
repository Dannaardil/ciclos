viaje_t = []
detener = 0

while True:
    tramos = int(input("ingrese el tramo: "))
    if tramos == detener:
        break
    
    viaje_t.append(tramos)
    print(viaje_t)
suma = sum(viaje_t)
hora = int(suma/60)
minutos= suma%60

print(f"tiempo total de viaje: {hora}:{minutos}")