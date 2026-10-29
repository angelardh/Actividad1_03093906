print("\n*** angela:    t03093906:    ***")
print("*** Nombre 2:    Matricula:    ***\n")

print("*** Ejercicio 10 Nivel de influencer ***")

#input() guarda texto; el usuario es texto, así que no lo convertimos
usuario = input("\nTu usuario: @")
#int() convierte a número entero para poder comparar
seguidores = int(input("¿Cuántos seguidores tienes? "))
#Si el usuario escribe 25000, ahora seguidores vale 25000

print(f"\n===== NIVEL DE @{usuario} =====")

#PREGUNTA 1: ¿25000 es menor que 1000? Respuesta: False, pasa a la siguiente
if seguidores < 1000:
    print("Nivel: Principiante")

#PREGUNTA 2: si llegamos aquí, YA SABEMOS que tiene 1000 o más
#¿25000 es menor que 10000? Respuesta: False, pasa a la siguiente
elif seguidores < 10000:
    print("Nivel: Microinfluencer")

#PREGUNTA 3: si llegamos aquí, YA SABEMOS que tiene 10000 o más
#¿25000 es menor que 100000? Respuesta: True, muestra el mensaje y TERMINA
elif seguidores < 100000:
    print("Nivel: Influencer")

#else: si ninguna fue True, tiene 100000 o más
else:
    print("Nivel: Celebridad digital")