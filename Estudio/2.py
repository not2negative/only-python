velocidades = [65.0, 82.5, 90.0, 110.4, 78.2, 125.0, 95.0]
infractores = []
suma_total = 0
contador = 0

for v in velocidades:
    suma_total += v
    if v > 90:
        infractores.append(v)
        contador += 1

promedio = round(suma_total / len(velocidades), 2)
print(f"Velocidad promedio: {promedio} Km/h")
print(f"Lista de infractores: {infractores} y han sido {contador} en total")