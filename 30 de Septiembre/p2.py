# Control de Calidad de Componentes
piezas = [5.05,4.98,5.12,5.25,5.01,4.90,5.18,5.08,5.30,5.15]
p_rechazadas = []

for p in piezas:
    if (p <= 5.0) or (p >= 5.2):
        p_rechazadas.append(p)

porc = (len(p_rechazadas) / len(piezas)) * 100
print(f"Mediciones totales: {piezas}")
print(f"Piezas rechazadas: {p_rechazadas}")
print(f"Porcentaje de piezas rechazadas: {porc}%")