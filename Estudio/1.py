print("=== TIPO DE CLIENTE ===")
print("1. Normal (Sin descuento)")
print("2. Estudiante (15% descuento)")
print("3. Tercera Edad (30% descuento)")

precio = float(input("\nIngrese el precio del producto: $"))
opcion = int(input("Ingrese una opción (1-3): "))
total = 0

match opcion:
    case 1:
        total = precio
        print(f"Cliente Normal. Total a pagar: ${total}")
    case 2:
        total += precio * 0.85
        print(f"Estudiante. Total a pagar: ${total}")
    case 3:
        total += precio * 0.70
        print(f"Tercera Edad. Total a pagar: ${total}")
    case _:
        print("Opción inválida. Debe ser entre 1 y 3.")
