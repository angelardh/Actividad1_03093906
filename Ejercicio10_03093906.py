print("Ejercicio 10: Permisos en el sistema de pedidos")
print("Nombre: Angela Delgado")
print("Matrícula: T03093906")
print()

# Permisos del sistema. Cada uno es un bit y los creamos con <<
VER = 1 << 0       # 0001 = 1
CREAR = 1 << 1     # 0010 = 2
APROBAR = 1 << 2   # 0100 = 4
EXPORTAR = 1 << 3  # 1000 = 8

print("Puestos: 1 = Practicante, 2 = Vendedor, 3 = Gerente")
puesto = input("Número de puesto del empleado: ")
capacitacion = input("¿Tomó la capacitación de comercio exterior? (si/no): ")
vacaciones = input("¿Está de vacaciones? (si/no): ")

# 1. Asigna los permisos de cada puesto juntándolos con |
#    Practicante: VER · Vendedor: VER y CREAR · Gerente: los 4 permisos
if puesto == "1":
    permisos = VER
elif puesto == "2":
    permisos = VER | CREAR
elif puesto == "3":
    permisos = VER | CREAR | APROBAR | EXPORTAR
else:
    permisos = 0
    print("❌ Puesto no válido. El empleado se queda sin permisos.")

# 2. Si tomó la capacitación, AGREGA el permiso de EXPORTAR (usa |)
if capacitacion == "si":
    permisos = permisos | EXPORTAR

# 3. Si está de vacaciones, QUITA el permiso de APROBAR (usa & y ~)
if vacaciones == "si":
    permisos = permisos & ~APROBAR

print()
print("===== PERMISOS DEL EMPLEADO =====")
print("Permisos finales:", format(permisos, "04b"), "=", permisos)

# 4. Revisa con & si tiene el permiso de EXPORTAR
if (permisos & EXPORTAR) != 0:
    print("🌐 Puede firmar pedimentos de exportación.")
else:
    print("🛑 No puede firmar pedimentos de exportación.")

# 5. Para liberar un pedido internacional necesita CREAR y EXPORTAR al mismo tiempo
requeridos = CREAR | EXPORTAR

# 6. Revisa que TODOS los bits de requeridos estén encendidos en permisos
if (permisos & requeridos) == requeridos:
    print("✅ Puede liberar pedidos internacionales.")
else:
    # 7. ¿Qué le falta? Los bits que están en requeridos pero NO en permisos (usa & y ~)
    faltan = requeridos & ~permisos
    print("🛑 No puede liberar pedidos internacionales. Le falta:", format(faltan, "04b"))
    
    if (faltan & CREAR) != 0:
        print("  - Permiso para crear pedidos")
    if (faltan & EXPORTAR) != 0:
        print("  - Permiso de exportación")