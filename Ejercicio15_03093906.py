print("\n*** Nombre 1:    Matricula:    ***")
print("*** Nombre 2:    Matricula:    ***\n")

print("*** Ejercicio 15 Rango en tu videojuego ***")

#int() convierte el texto a número entero para poder comparar y hacer cuentas
puntos = int(input("\n¿Cuántos puntos tienes? "))
#Si el usuario escribe 2500, ahora puntos vale 2500

print("\n===== TU RANGO =====")

#Empezamos por el rango MÁS ALTO
#¿2500 es mayor o igual que 3000? False, pasa a la siguiente
if puntos >= 3000:
    print("Rango: DIAMANTE")
    print("¡Ya estás en el rango máximo!")

#¿2500 es mayor o igual que 2000? True, entra aquí y TERMINA
elif puntos >= 2000:
    #Esta fórmula dice: faltan = 3000 - 2500
    faltan = 3000 - puntos
    #Ahora faltan vale 500
    print("Rango: ORO")
    print(f"Te faltan {faltan} puntos para Diamante")

elif puntos >= 1000:
    faltan = 2000 - puntos
    print("Rango: PLATA")
    print(f"Te faltan {faltan} puntos para Oro")

#else: tiene menos de 1000
else:
    faltan = 1000 - puntos
    print("Rango: BRONCE")
    print(f"Te faltan {faltan} puntos para Plata")