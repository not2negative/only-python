# Búsqueda del Sensor con Mayor Consumo
consumos = [120.5,340.2,85.0,510.8,230.4,490.1]
max_consumo = consumos[0]
max_pos = 0

for pos,consumo in enumerate(consumos):
    if consumo > max_consumo:
        max_consumo = consumo
        max_pos = pos

print(f"Registro de consumos: {consumos}")
print(f"El mayor consumo fue de: {max_consumo} W y corresponde a la posición {max_pos + 1}")