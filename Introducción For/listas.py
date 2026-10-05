# Iteración sobre secuencias
# Una lista/arreglo/array/matriz sirve para almacenar datos en una sola variable
# Se denomina array/arreglo o arregllo unidimensional porque son una colección de elementos dispuestos en un orden secuencial
# Se le puede denominar también como matriz unidimensional ya que solo trabaja en una línea de datos o vector
# Recorriendo una lista
temperaturas = [18.5, 21.0, 19.3, 24.1] # Primero se hace una lista donde estan las variables (estos números son ejemplos)

for temp in temperaturas: # Posteriormente se llamará la lista de temperaturas y será recorrida con una variable con nombre cualquiera
    print(f"Temperaturas registradas: {temp}")

print("\n====================\n")

# Recorriendo una cadena de texto o String
cod_sensor = "SENSOR_01"

for char in cod_sensor:
    print(f"Carácter: {char}")

print("\n====================\n")

# Recorriendo una tupla
coordenadas = (-33.45,-70.66) # Una tupla es una lista inmutable, osea que no se puede modificar su contenido
for componente in coordenadas:
    print(f"Coordenada: {componente}")