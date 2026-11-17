print("Ejercicio 7: Zona de envío y costo del flete")
print("Nombre: Angela Delgado")
print("Matrícula: T03093906")
print()

# Pedimos los datos del pedido
pais = input("País destino en MAYÚSCULAS y sin acento: ")
kilos = float(input("Peso del pedido en kg: "))
frecuente = input("¿Es cliente frecuente? (si/no): ")
urgente = input("¿El pedido es urgente? (si/no): ")

# Convertimos las respuestas en True o False
es_frecuente = frecuente == "si"
es_urgente = urgente == "si"

print()
print("===== COTIZACIÓN DEL FLETE =====")

# or con comparaciones: cada lado del or es una comparación COMPLETA
if pais == "ESTADOS UNIDOS" or pais == "CANADA":
    zona = "NORTEAMERICA"
    tarifa = 2
elif pais == "GUATEMALA" or pais == "COLOMBIA" or pais == "CHILE" or pais == "BRASIL":
    zona = "LATINOAMERICA"
    tarifa = 3
elif pais == "ALEMANIA" or pais == "FRANCIA" or pais == "ITALIA":
    zona = "EUROPA"
    tarifa = 5
else:
    zona = "SIN RUTA"
    tarifa = 0

if zona == "SIN RUTA":
    print("❌ No tenemos ruta de envío a", pais)
else:
    flete = kilos * tarifa
    print("Zona:", zona)
    print("Flete: $", flete, sep="")

    # or: si es urgente O pesa más de 1000 kg, se cobra un cargo especial
    if es_urgente or kilos > 1000:
        cargo = 500
        print("➕ Cargo especial (urgente o más de 1000 kg): $500")
    else:
        cargo = 0

    subtotal = flete + cargo

    # or: si es cliente frecuente O el subtotal pasa de $5000, hay descuento
    if es_frecuente or subtotal > 5000:
        descuento = subtotal * 10 / 100
        print("🎁 Descuento del 10%: $", descuento, sep="")
    else:
        descuento = 0

    total = subtotal - descuento
    print("Total a pagar: $", total, sep="")