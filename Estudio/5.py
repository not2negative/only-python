# Entrada
productos = ["Laptop", "Mouse", "Teclado", "Monitor", "Audífonos"]
stock = [5,22,8,3,15]
precios_unitarios = [850000, 15000, 35000, 190000, 45000]

# Procesamiento
# Requerimiento 1
valores_totales = []
for s,p in zip(stock,precios_unitarios):
    valores_totales.append(s * p)

# Requerimiento 2
suma_total_bodega = 0
for i in valores_totales:
    suma_total_bodega += i

# Requerimiento 3
reabastecer = []
for prod,s in zip(productos,stock):
    if s < 10:
        reabastecer.append(prod)

# Requerimiento 4
max_valor = valores_totales[0]
max_pos = 0
for pos,val in enumerate(valores_totales):
    if val > max_valor:
        max_valor = val
        max_pos = pos

# Salida
print(f"Valores totales por producto: {valores_totales}")
print(f"Valor total invertido en bodega: {suma_total_bodega}")
print(f"Productos que requieren reabastecimiento: {reabastecer}")
print(f"El producto con mayor capital invertido es: {productos[max_pos]} con ${max_valor}")