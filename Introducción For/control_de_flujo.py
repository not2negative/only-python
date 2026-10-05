# Los controles de flujo sirven para (como su nombre indica) controlar como funciona un algoritmo o bloque de iteración
# Break: Interrumpe el bucle y sale de forma inmediata.
puertos = [80,443,8080,21,22]

for puerto in puertos:
    if puerto == 21:
        print(f"Puerto inseguro detectado (21): deteniendo escaneo...")
        break
    print(f"Puerto {puerto} verificado")

print("\n")

# Sin el break solo imprimiría (en este caso) el mensaje del puerto inseguro pero no pararía el escaneo
for puerto in puertos:
    if puerto == 21:
        print(f"Puerto inseguro detectado (21): deteniendo escaneo...")
        
    print(f"Puerto {puerto} verificado")

print("\n====================\n")

# Continue: Salta el resto del código de la iteración actual y pasa a la siguiente
voltajes = [110,0,115,-5,120]

for v in voltajes:
    if v <= 0:
        print(f"Lectura anómala detectada (nula u omitida)")
        continue
    print(f"Voltaje procesado: {v} V")

print("\n")

# Sin el continue pasa lo mismo que el ejemplo anterior: la condición del IF se vuelve verdadera e imprime la lectura anómala pero sigue de largo
for v in voltajes:
    if v <= 0:
        print(f"Lectura anómala detectada (nula u omitida)")
        
    print(f"Voltaje procesado: {v} V")

# === === === === === === === === === === ===

"""
¿Cuando usar cada tipo de for?
- Usa "for x in colección" cuando quieras los elementos
- Usa "for i in range(n)" cuado necesites repetir n veces
- Usa "for i,x in enumerate(colección)" cuando necesites índices y elementos
- USa "for a,b in zip(colección1,colección2) cuando quieras procesar dos colecciones a la vez
"""

# === === === === === === === === === === ===

"""
Un for se compone exactamente así

for "variable_de_control" in "iterable":
    "Bloque de código indentado"
    "Instrucciones a repetir"
"""