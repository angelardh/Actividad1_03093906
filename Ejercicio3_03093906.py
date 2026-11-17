print("Ejercicio 3: ¿Se puede exportar el producto?")
print("Nombre: Angela Delgado")
print("Matrícula: 03093906")
print()

# Pedimos los datos del producto y del destino
producto = input("¿Qué producto vas a exportar?: ")
respuesta1 = input("¿Está en la lista de restringidos? (si/no): ")
respuesta2 = input("¿La empresa tiene permiso especial? (si/no): ")
respuesta3 = input("¿El permiso está vigente? (si/no): ")
respuesta4 = input("¿El país destino tiene restricciones comerciales? (si/no): ")
kilos = float(input("¿Cuántos kilos vas a enviar?: "))

# Convertimos las respuestas en True o False
restringido = respuesta1 == "si"
tiene_permiso = respuesta2 == "si"
permiso_vigente = respuesta3 == "si"
destino_restringido = respuesta4 == "si"

# Un permiso solo sirve si existe Y está vigente
permiso_valido = tiene_permiso and permiso_vigente

print()
print("===== REVISIÓN DE CUMPLIMIENTO =====")

# Se exporta si: (NO está restringido O tiene permiso válido) Y el destino NO tiene restricciones
if (not restringido or permiso_valido) and not destino_restringido:
    print("✅", producto, "se puede exportar.")

    # and: restringido Y más de 1000 kilos: necesita inspección
    if restringido and kilos > 1000:
        print("🔍 Por ser restringido y pesar más de 1000 kg, necesita inspección previa.")
else:
    print("🛑", producto, "NO se puede exportar.")

    # Explicamos el motivo
    if destino_restringido:
        print("Motivo: el país destino tiene restricciones comerciales.")
    elif not tiene_permiso:
        print("Motivo: el producto está restringido y no hay permiso especial.")
    elif not permiso_vigente:
        print("Motivo: el permiso especial está vencido. Hay que renovarlo.")