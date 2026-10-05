temperaturas = [18.4, 12.1, 15.6, 9.8, 14.2]
min_temp = temperaturas[0]
min_pos = 0

for pos,temp in enumerate(temperaturas):
    if temp < min_temp:
        min_temp = temp
        min_pos = pos

print(f"la temperatura más baja es de {min_temp} C° y está en la posición {min_pos + 1}")