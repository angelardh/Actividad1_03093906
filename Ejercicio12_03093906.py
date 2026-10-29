print("\n*** angela:    t03093906:    ***")
print("*** Nombre 2:    Matricula:    ***\n")

print("*** Ejercicio 12 Playlist según tu mood ***")

#Mostramos el menú de opciones
print("\n===== ¿CÓMO TE SIENTES HOY? =====")
print("1 = Feliz")
print("2 = Triste")
print("3 = Con energía")
print("4 = Estudiando")

#int() convierte el texto a número para compararlo con 1, 2, 3 y 4
mood = int(input("\nEscribe el número de tu mood: "))
#Si el usuario escribe 4, ahora mood vale 4

#Python revisa en orden y se detiene en la primera que sea True
#¿4 es igual a 1? False, pasa a la siguiente
if mood == 1:
    print("Te recomiendo una playlist de pop")
#¿4 es igual a 2? False, pasa a la siguiente
elif mood == 2:
    print("Te recomiendo una playlist de baladas")
#¿4 es igual a 3? False, pasa a la siguiente
elif mood == 3:
    print("Te recomiendo una playlist de reggaetón o K-pop")
#¿4 es igual a 4? True, muestra el mensaje y TERMINA
elif mood == 4:
    print("Te recomiendo una playlist de lo-fi para concentrarte")
#else: escribió un número que no está en el menú
else:
    print("Ese mood no está en la lista")