# Monitoreo de Temperatura en un Servidor
temperaturas = [38.5, 42.0, 46.2, 44.8, 48.1, 41.3, 39.0, 47.5]
suma_total = 0
contador = 0

for t in temperaturas:
    suma_total += t
    if t > 45:
        contador += 1

promedio = suma_total / len(temperaturas)
print(f"Cantidad de veces que supero el umbral crítico: {contador} veces")
print(f"Promedio de temperaturas: {promedio} C°")