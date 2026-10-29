print("\n*** Angela:    t03093906:    ***")
print("*** Nombre 2:    Matricula:    ***\n")

print("*** Ejercicio 9 Tamaño de tu bebida ***")

#Mostramos el menú para que el usuario sepa qué puede elegir
print("\n===== MENÚ DE TAMAÑOS =====")
print("1 = Chico   ($55)")
print("2 = Mediano ($70)")
print("3 = Grande  ($85)")

#input() pregunta y guarda la respuesta como TEXTO
#int() la convierte a número entero para poder compararla con 1, 2 y 3
opcion = int(input("\n¿Qué tamaño quieres? Escribe 1, 2 o 3: "))
#Si el usuario escribe 2, ahora opcion vale 2

#PREGUNTA 1: ¿2 es igual a 1? Respuesta: False, entonces pasa a la siguiente pregunta
if opcion == 1:
    print("Elegiste tamaño CHICO, son $55")

#PREGUNTA 2: ¿2 es igual a 2? Respuesta: True, entonces muestra este mensaje
#y Python YA NO revisa las preguntas de abajo
elif opcion == 2:
    print("Elegiste tamaño MEDIANO, son $70")

#PREGUNTA 3: solo se revisa si las dos anteriores fueron False
elif opcion == 3:
    print("Elegiste tamaño GRANDE, son $85")

#else: entra aquí solo si NINGUNA pregunta fue True (escribió 4, 7, 0, etc.)
else:
    print("Opción no válida, elige 1, 2 o 3")

#Esta línea no tiene sangría, no pertenece al if, por eso se muestra siempre
print("\n¡Gracias por tu compra!")