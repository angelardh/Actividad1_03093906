print("\n===================================================")
print("Ejercicio 9: Tienda de mascotas interactiva")
print("TIENDA DE MASCOTAS DE MiNombre")

#input() le pregunta al usuario y guarda lo que escribe en la variable
#input() SIEMPRE guarda TEXTO, aunque escribas un número
mascota = input("\n¿Qué mascota quieres adoptar? ")
#Si el usuario escribe gato, ahora mascota vale "gato"


#float() convierte el texto a número con decimales para poder hacer cuentas
precio_mascota = float(input(f"¿Cuánto cuesta el/la {mascota}? $"))
#Si el usuario escribe 1500, ahora precio_mascota vale 1500.0

precio_croquetas = float(input("¿Cuánto cuesta un mes de croquetas? $"))
#Si el usuario escribe 350, ahora precio_croquetas vale 350.0

#int() convierte el texto a número entero, porque los meses no llevan decimales
meses = int(input("¿Para cuántos meses quieres croquetas? "))
#Si el usuario escribe 3, ahora meses vale 3


#Calculamos cuánto gasto en croquetas, esta formula dice: costo_croquetas = 350.0 * 3
costo_croquetas = precio_croquetas * meses
#Ahora costo_croquetas vale 1050.0


#Calculamos el total, esta formula dice: total = 1500.0 + 1050.0
total = precio_mascota + costo_croquetas
#Ahora total vale 2550.0


print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("Ticket de compra")

#El :.2f muestra 2 decimales, como se ve el dinero
print(f"Mascota: {mascota}   ${precio_mascota:.2f}")
print(f"Croquetas por {meses} meses: ${costo_croquetas:.2f}")
print(f"\nTOTAL A PAGAR: ${total:.2f}\n")

print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")