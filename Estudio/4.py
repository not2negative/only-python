mes_1 = [1200, 1500, 900, 2100]
mes_2 = [1350, 1400, 1100, 2500]
ventas_totales = []

for v1,v2 in zip(mes_1,mes_2):
    v = v1 + v2
    ventas_totales.append(v)

print(f"Las ventas totales han sido de: {ventas_totales}")