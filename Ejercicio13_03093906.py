print("\n*** angela:    t03093906:    ***")
print("*** Nombre 2:    Matricula:    ***\n")

print("*** Ejercicio 13 Mensaje según tu calificación ***")

#int() convierte el texto a número entero para poder comparar
calificacion = int(input("\n¿Qué calificación sacaste en el examen de Cisco? "))
#Si el usuario escribe 85, ahora calificacion vale 85

print("\n===== RESULTADO =====")

#PRIMERO revisamos que la calificación sea válida
#¿85 es mayor que 100? False, pasa a la siguiente
if calificacion > 100:
    print("Calificación no válida, debe ser de 0 a 100")

#¿85 es menor que 0? False, pasa a la siguiente
elif calificacion < 0:
    print("Calificación no válida, debe ser de 0 a 100")

#Si llegamos aquí, YA SABEMOS que la calificación es válida
#¿85 es mayor o igual que 90? False, pasa a la siguiente
elif calificacion >= 90:
    print("¡Excelente! Eres crack")

#¿85 es mayor o igual que 80? True, muestra el mensaje y TERMINA
elif calificacion >= 80:
    print("Muy bien")

#Ya sabemos que es menor que 80
elif calificacion >= 70:
    print("Aprobaste, pero puedes mejorar")

#else: es menor que 70
else:
    print("Reprobaste, ¡a estudiar!")