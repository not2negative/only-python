# Iteración sobre rangos númericos
# Bucle solo con range(stop)
for i in range(5):
    print(f"Iteracion número: {i}")

print("\n====================\n")

# Bucle tradicional con range(start, stop)
for i in range(0,5):
    print(f"Iteracion número: {i}")

print("\n====================\n")

# Bucle tomando encuenta el último número del range(start, stop)
for i in range(0,5 + 1):
    print(f"Iteracion número: {i}")

print("\n====================\n")

# Bucle con range(start, stop, step)
for i in range(0,5,2):
    print(f"Iteracion número: {i}")

print("\n====================\n")

# Bucle de cuenta regresiva sencillo
for i in range(5,0,-1):
    print(f"Contador: {i}")

print("\n====================\n")

# Bucle de cuenta regresiva con número final incluido
for i in range(5,0 - 1,-1):
    print(f"Contador: {i}")