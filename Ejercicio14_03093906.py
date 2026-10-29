print("\n*** angela:    t03093906:    ***")
print("*** Nombre 2:    Matricula:    ***\n")

print("*** Ejercicio 14 Costo de envío ***")

#float() convierte a número con decimales, porque el dinero y los km pueden tener decimales
pedido = float(input("\n¿Cuánto es tu pedido? $"))
#Si el usuario escribe 250, ahora pedido vale 250.0
distancia = float(input("¿A cuántos km vives de la tienda? "))
#Si el usuario escribe 8, ahora distancia vale 8.0

#En cada opción GUARDAMOS el costo de envío en la misma variable
#¿8.0 es menor o igual que 3? False, pasa a la siguiente
if distancia <= 3:
    costo_envio = 0
    print("\n¡Envío gratis!")

#¿8.0 es menor o igual que 10? True, guarda 39 y TERMINA
elif distancia <= 10:
    costo_envio = 39
    print("\nEl envío cuesta $39")

elif distancia <= 20:
    costo_envio = 69
    print("\nEl envío cuesta $69")

#else: vive a más de 20 km
else:
    costo_envio = 0
    print("\nNo hacemos envíos a más de 20 km, recoge tu pedido en tienda")

#Esta parte no tiene sangría, se hace SIEMPRE
#Ahora costo_envio vale 39, esta fórmula dice: total = 250.0 + 39
total = pedido + costo_envio
print(f"Pedido: ${pedido:.2f}")
print(f"Envío: ${costo_envio:.2f}")
print(f"TOTAL A PAGAR: ${total:.2f}")