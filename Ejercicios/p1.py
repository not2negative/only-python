# Monitoreo de Temperatura en un Servidor (Procesamiento de Secuencias)
temperaturas = [42.1,98.4,34.5,67.8,56.6,53.5,23.4,12.6]
suma = 0
contador_critico = 0

for temp in temperaturas:
    suma += temp
    if temp > 45:
        contador_critico += 1

prom = round(suma / len(temperaturas),2)

print(f"El promedio de la temperatura fue: {prom} C°.")
print(f"Las temperaturas superaron el umbral crítico {contador_critico} veces.")