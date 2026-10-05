# Cálculo de Carga Neta en una Estructura (Suma Elemento a Elemento / Vectores Paraleos)
cargas_vivas = [15.2, 23.4, 11.2, 34.8, 20.5] # kN
cargas_muertas = [20, 23.8, 49.5, 50, 60] # kN
carga_total = []

for viva, muerta in zip(cargas_vivas, cargas_muertas):
    nueva_carga = (1.2 * muerta) + (1.6 * viva)
    carga_total.append(nueva_carga)

print(f"Cargas vivas son: {cargas_vivas}")
print(f"Cargas muertas son: {cargas_muertas}")
print(f"Vector de carga total: {carga_total}")