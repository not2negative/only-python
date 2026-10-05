# Sirve por si se necesita procesar los elementos de una secuencia/lista/diccionario y al mismo tiempo conocer su posición (indice) que ocupan
# Por ejemplo
estudiantes = ["Ana","Carlos","Beatriz","Diego"] # Creamos una lista (en este caso con strings)

for indice, nombre in enumerate(estudiantes): # Inventamos dos variables de control y con el operador in dentro del iterable "enumerate"
    print(f"Posición {indice + 1}: {nombre}") # Se le añade el + 1 en el indice para que no empiece en el 0

print("\n====================\n")

for indice, nombre in enumerate(estudiantes):
    print(f"Posición {indice}: {nombre}") # En este caso si empieza en el 0