print("Ejercicio 11: Revisión de pedido y reporte de ventas")
print("Nombre: Angela Delgado")
print("Matrícula: T03093906")
print()

# Listas de la empresa
catalogo = ["CAFE", "TEQUILA", "MIEL", "AGUACATE", "ACIDO SULFURICO"]
restringidos = ["ACIDO SULFURICO", "MERCURIO", "PIROTECNIA"]
paises_tmec = ["MEXICO", "ESTADOS UNIDOS", "CANADA"]

# Ventas del cliente de enero a junio, en miles de dólares
ventas = [120, 95, 140, 160, 110, 175]

# Pedimos los datos del pedido
producto = input("Producto en MAYÚSCULAS y sin acento: ")
pais = input("País destino en MAYÚSCULAS y sin acento: ")
meses = int(input("¿Cuántos meses quieres en el reporte? (1 a 6): "))

print()
print("===== REVISIÓN DEL PEDIDO =====")

# not in: si el producto NO está en el catálogo, la empresa no lo vende
if producto not in catalogo:
    print("❌", producto, "no está en nuestro catálogo.")
else:
    # in: ¿el producto está en la lista de restringidos?
    if producto in restringidos:
        print("🔴", producto, "necesita permiso especial para exportarse.")
    else:
        print("✅", producto, "se puede exportar sin permiso especial.")

    # in: ¿el país destino está en el T-MEC?
    if pais in paises_tmec:
        print("🌎", pais, "está en el T-MEC: arancel 0%.")
    else:
        print("📄", pais, "no está en el T-MEC: se cobra el arancel general.")

print()
print("===== REPORTE DE VENTAS DEL CLIENTE =====")

# or: los meses deben estar entre 1 y 6
if meses < 1 or meses > 6:
    print("❌ Escribe un número de meses entre 1 y 6.")
else:
    # Rebanada sin inicio: los primeros 'meses' meses
    print("Primeros", meses, "meses:", ventas[:meses])

    # Rebanada con número negativo: los últimos 'meses' meses
    print("Últimos", meses, "meses:", ventas[-meses:])

    # Rebanadas fijas: los dos trimestres del semestre
    print("Primer trimestre:", ventas[0:3])
    print("Segundo trimestre:", ventas[3:6])