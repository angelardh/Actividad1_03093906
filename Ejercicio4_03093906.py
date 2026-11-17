print("Ejercicio 4: Semáforo de revisión aduanal")
print("Nombre: Angela Delgado")
print("Matrícula: 03093906")
print()

# Pedimos los datos del embarque y de la empresa
valor = float(input("Valor del embarque en dólares: "))
primera = input("¿Es la primera vez que la empresa importa? (si/no): ")
certificada = input("¿La empresa está certificada como confiable? (si/no): ")
documentos = input("¿Los documentos están completos? (si/no): ")
perecedero = input("¿La mercancía es perecedera (fruta, flores, carne)? (si/no): ")

# Convertimos a True o False
es_primera = primera == "si"
es_certificada = certificada == "si"
documentos_ok = documentos == "si"
es_perecedero = perecedero == "si"

print()
print("===== SEMÁFORO ADUANAL =====")

# ROJO si: los documentos NO están completos
# O (es caro O es su primera vez) y además NO está certificada
if not documentos_ok or ((valor > 50000 or es_primera) and not es_certificada):
    print("🔴 Semáforo ROJO: el embarque pasa a revisión física.")
    dias = 3

    # and: rojo Y perecedero: la mercancía se puede echar a perder
    if es_perecedero:
        print("⚠️ Mercancía perecedera: solicita revisión prioritaria.")
        dias = 1
else:
    print("🟢 Semáforo VERDE: el embarque pasa sin revisión.")
    dias = 0

# Cada día en la aduana cuesta $500 de almacenaje
almacenaje = dias * 500
print("Días estimados en la aduana:", dias)
print("Costo de almacenaje: $", almacenaje, sep="")