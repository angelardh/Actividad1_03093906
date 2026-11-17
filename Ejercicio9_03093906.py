print("Ejercicio 9: Requisitos de aduana en un solo número")
print("Nombre: angela Delgado")
print("Matrícula: T03093906")
print()

# Cada requisito es un bit. Los creamos con << (correr un 1 a la izquierda)
FACTURA = 1 << 0  # 0001 = 1
PEDIMENTO = 1 << 1  # 0010 = 2
IMPUESTOS = 1 << 2  # 0100 = 4
MERCANCIA = 1 << 3  # 1000 = 8

# | : juntamos los 4 bits para saber cómo se ve un embarque completo
TODOS = FACTURA | PEDIMENTO | IMPUESTOS | MERCANCIA  # 1111 = 15

# Pedimos los requisitos
factura = input("¿Tienes la factura comercial? (si/no): ")
pedimento = input("¿Tienes el pedimento de importación? (si/no): ")
impuestos = input("¿Ya pagaste los impuestos? (si/no): ")
coincide = input("¿La mercancía coincide con lo declarado? (si/no): ")

# Empezamos con todos los bits apagados y prendemos con | cada requisito cumplido
codigo = 0
if factura == "si":
    codigo = codigo | FACTURA
if pedimento == "si":
    codigo = codigo | PEDIMENTO
if impuestos == "si":
    codigo = codigo | IMPUESTOS
if coincide == "si":
    codigo = codigo | MERCANCIA

print()
print("===== RESULTADO DE LA ADUANA =====")
print("Código del embarque:", format(codigo, "04b"), "=", codigo)

# & : si al comparar con TODOS el resultado es TODOS, no falta ningún bit
if (codigo & TODOS) == TODOS:
    print("✅ Embarque liberado. Puede salir de la aduana.")
else:
    # ~ y & : invertimos el código para ver los bits que están en 0 (lo que falta)
    faltan = ~codigo & TODOS
    print("🛑 Embarque detenido. Código de lo que falta:", format(faltan, "04b"))

    if (faltan & FACTURA) != 0:
        print("  - Factura comercial")
    if (faltan & PEDIMENTO) != 0:
        print("  - Pedimento de importación")
    if (faltan & IMPUESTOS) != 0:
        print("  - Pago de impuestos")
    if (faltan & MERCANCIA) != 0:
        print("  - La mercancía no coincide con lo declarado")