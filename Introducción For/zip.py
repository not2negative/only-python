# Iteración con zip
# Se usa para iterar dos o más iterables de forma simultánea en una sola instrucción
# En este ejemplo lo haremos con 2 listas
sensores = ["Sensor_norte","Sensor_sur","Sensor_este","Sensor_oeste"]
lecturas = [23.4,19.8,22.1,29.3]

# Unimos ambas listas para procesarlas en pares
for sensor,lectura in zip(sensores,lecturas):
    print(f"El {sensor} reporta una lectura de {lectura} unidades")