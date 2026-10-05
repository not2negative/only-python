# Cálculo de Carga Neta en una Estructura
cargas_vivas = [50.2,32.3,38.5,60.6,45.4]
cargas_muertas = [80.9,93.9,90.7,87.6,83.3]
carga_total = []

for i1,i2 in zip(cargas_vivas,cargas_muertas):
    i_total = round((1.2 * i2) + (1.6 * i1),2)
    carga_total.append(i_total)

print(f"Cargas vivas: {cargas_vivas}")
print(f"Cargas muertas: {cargas_muertas}")
print(f"Carga total: {carga_total}")