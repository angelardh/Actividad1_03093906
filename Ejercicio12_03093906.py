print("Ejercicio 12: Precios del Buen Fin")
print("Nombre: Angela Delgado")
print("Matrícula: T03093906")
print()

# Catálogo: cada producto tiene su precio en la MISMA posición
productos = ["Café", "Tequila", "Miel", "Mezcal", "Cacao"]
precios = [450, 1200, 300, 980, 150]

# Pedimos los datos
descuento = float(input("Porcentaje de descuento del Buen Fin: "))
consulta = input("¿Qué producto quiere consultar el cliente?: ")

# 1. Haz una COPIA REAL de precios para no cambiar los precios originales
promocion = list(precios)

# Aplicamos el descuento a cada precio de la copia
for i in range(len(promocion)):
    promocion[i] = promocion[i] - promocion[i] * descuento / 100

# 2. Solo los 3 PRIMEROS productos entran a la promoción. Toma ese pedazo con una rebanada
productos_promo = productos[:3]

# 3. Borra de promocion los precios desde la posición 3 hasta el final (usa del)
del promocion[3:]

print()
print("===== PRECIOS DEL BUEN FIN =====")
print("Productos en promoción:", productos_promo)
print("Precios originales:", precios)
print("Precios con descuento:", promocion)

# 4. Busca el producto más caro de la promoción
mayor = promocion[0]
pos_mayor = 0
for i in range(len(promocion)):
    if promocion[i] > mayor:
        mayor = promocion[i]
        pos_mayor = i
print("⭐ El producto en promoción más caro es ", productos_promo[pos_mayor], " a $", mayor, sep="")

print()
print("===== CONSULTA DEL CLIENTE =====")

# 5. Si el producto NO está en el catálogo, avisa al cliente
if consulta not in productos:
    print("❌", consulta, "no está en nuestro catálogo.")
else:
    # Buscamos la posición del producto en el catálogo
    pos = -1
    for i in range(len(productos)):
        if productos[i] == consulta:
            pos = i
            
    print("Precio normal de ", consulta, ": $", precios[pos], sep="")

    # 6. Revisa si el producto está en la lista de productos en promoción
    if consulta in productos_promo:
        print("🎉 Precio Buen Fin: $", promocion[pos], sep="")
    else:
        print("📄", consulta, "no entra a la promoción. Se cobra el precio normal.")