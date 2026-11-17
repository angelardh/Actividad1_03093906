print("Ejercicio 8: Servicios de dos navieras")
print("Nombre: Angela Delgado")
print("Matrícula: T03093906")
print()

# Cada servicio es un bit (un interruptor de sí o no):
#   1 = Flete   2 = Seguro   4 = Despacho aduanal   8 = Almacenaje
# Si una naviera ofrece Flete y Despacho, su código es 1 + 4 = 5 (binario 0101)
print("Servicios: 1 = Flete, 2 = Seguro, 4 = Despacho aduanal, 8 = Almacenaje")
naviera_a = int(input("Código de servicios de la Naviera A (0 a 15): "))
naviera_b = int(input("Código de servicios de la Naviera B (0 a 15): "))

# & : el bit queda en 1 solo si está en 1 en LAS DOS navieras
en_comun = naviera_a & naviera_b

# | : el bit queda en 1 si está en 1 en AL MENOS UNA naviera
entre_las_dos = naviera_a | naviera_b

# ^ : el bit queda en 1 si está en 1 en UNA SOLA naviera (no en las dos)
solo_una = naviera_a ^ naviera_b

print()
print("===== COMPARACIÓN DE NAVIERAS =====")
# format(numero, "04b") muestra el número en binario con 4 dígitos
print("Naviera A:       ", format(naviera_a, "04b"))
print("Naviera B:       ", format(naviera_b, "04b"))
print("A & B (las dos): ", format(en_comun, "04b"), "=", en_comun)
print("A | B (al menos una): ", format(entre_las_dos, "04b"), "=", entre_las_dos)
print("A ^ B (solo una):   ", format(solo_una, "04b"), "=", solo_una)

print()
print("Servicios que ofrecen LAS DOS navieras:")
# & con un solo bit: si el resultado NO es 0, ese servicio está encendido
if (en_comun & 1) != 0:
    print("  - Flete")
if (en_comun & 2) != 0:
    print("  - Seguro")
if (en_comun & 4) != 0:
    print("  - Despacho aduanal")
if (en_comun & 8) != 0:
    print("  - Almacenaje")
if en_comun == 0:
    print("  - Ninguno. Las navieras no tienen servicios en común.")