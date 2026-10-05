# Inversión de Datos en un Buffer de Telecomunicaciones (Inversión de Arrays)
paquetes = [10,20,30,40,50,60,70]
paquetes_invertidos = []

for p in range(len(paquetes)-1,-1,-1):
    paquetes_invertidos.append(paquetes[p])

print(f"Resultado: {paquetes_invertidos}")

print("\n====================\n")

# Con reverse
paquetes = [10,20,30,40,50,60,70]
paquetes_invertidos = []

for p in reversed(paquetes):
    paquetes_invertidos.append(p)

print(f"Resultado: {paquetes_invertidos}")