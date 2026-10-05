# Búsqueda del Sensor con Mayor Consumo (Búsqueda de Máximo e Índice)
consumos = [110.4,105.4,220.0,109.5,204.9,100.0]
consumo_maximo = consumos[0]
indice_maximo = 0

for i in range(1,len(consumos)):
    if consumos[i] > consumo_maximo:
        consumo_maximo = consumos[i]
        indice_maximo = i

print(f"El mayor consumo fue de: {consumo_maximo} W")
print(f"Corresponde al sensor {indice_maximo + 1}")