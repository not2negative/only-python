# Control de Calidad de Componentes (Filtrado de Datos)
piezas = [5.1, 5.2, 5.5, 6.8, 5.1, 1.4, 5.0, 9.2, 1.4, 5.3]
piezas_rechazadas = []

for pieza in piezas:
    if (pieza < 5.0) or (pieza > 5.2):
        piezas_rechazadas.append(pieza)

porc = (len(piezas_rechazadas) / len(piezas)) * 100
print(f"Piezas rechazadas: {piezas_rechazadas}")
print(f"{porc}%")

print("\n====================\n")

# Forma simple
parts = [5.5,3.4,5.1,5.1,5.0,6.7,5.2,5.0,5.1,4.7] # Lista de partes funcionales
rejected = [] # Lista de rechazados
counter = 0 # Se predefine una variable contadora con un int inicial de 0

for cell in parts: # Cell para referirse a las celdas dentro de la lista de piezas
    if (cell < 5.0) or (cell > 5.2):
        rejected.append(cell) # .append() agrega elementos a una lista
        counter += 1 # Cuenta los rechazados

percentage = counter * 10 # Calcúla el porcentaje en base del contador y lo multiplica por 10 NO por 100
print(f"Matriz pieza {parts}")
print(f"Matriz rechazados {rejected}")
print(f"El porcentaje de rechazados es del {percentage}%")