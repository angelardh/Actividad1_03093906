print("\n************************************************************")
print("Ejercicio 10: Reto final, ¿soy viral?")
print("CALCULADORA DE ENGAGEMENT HECHO POR ANGELA")


#input() guarda texto, aquí no convertimos porque el usuario es texto
#Si el usuario escribe mi_cuenta, ahora usuario vale "mi_cuenta"
usuario = input("\nTu usuario de Instagram/TikTok: @")


#int() convierte el texto a número entero para poder hacer cuentas
#Si el usuario escribe 800, ahora seguidores vale 800
seguidores = int(input("¿Cuántos seguidores tienes? "))

#Si el usuario escribe 60, ahora likes vale 60
likes = int(input("¿Cuántos likes tuvo tu último post? "))

#Si el usuario escribe 12, ahora comentarios vale 12
comentarios = int(input("¿Cuántos comentarios tuvo? "))


#Sumamos todas las interacciones, esta formula dice: interacciones = 60 + 12
#Ahora interacciones vale 72
interacciones = likes + comentarios


#Calculamos el engagement: qué porcentaje de mis seguidores interactuó
#Los paréntesis hacen que la división se haga ANTES de multiplicar por 100
#Esta formula dice: engagement = (72 / 800) * 100, o sea 0.09 * 100
engagement = (interacciones / seguidores) * 100

#Ahora engagement vale 9.0


print(f"\n**************** RESULTADOS DE @{usuario} ****************")
print(f"Interacciones totales: {interacciones}")

#El :.2f muestra 2 decimales, así que se ve 9.00%
print(f"Engagement: {engagement:.2f}%")

print("\nDato: en redes, un engagement arriba de 3% ya se considera bueno")
print("\n************************************************************")