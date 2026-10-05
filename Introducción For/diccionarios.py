# Iteración sobre diccionarios
# Los diccionarios son listas pero almacenan pares así "clave: valor"
# Podemos iterar sobre sus claves o sus valores o ambos al mismo tiempo

rendimiento_servidores = {
    "Servidor_A": 85.5,
    "Servidor_B": 92.0,
    "Servidor_C": 78.1
}

# OJO: Las claves pueden tomar cualquier tipo de dato (int, float, bool, etc.) y lo mismo con los valores

# Tomando el ejemplo anterior vamos a iterar
# Recorriendo solo claves
for servidor in rendimiento_servidores:
    print(f"Nombre del servidor: {servidor}")

print("\n====================\n")

# Iterando solo sobre valores
for uso_cpu in rendimiento_servidores.values(): # Usamos el .values() para llamar SOLO los valores de un diccionario
    print(f"Uso del CPU: {uso_cpu}%")

print("\n====================\n")

# Iterando sobre las claves y los valores a la vez
for servidor, uso_cpu in rendimiento_servidores.items():
    print(f"El {servidor} presenta un uso de CPU del {uso_cpu}%")