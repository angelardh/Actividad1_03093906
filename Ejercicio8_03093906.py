print("\n************************************************************")
print("Ejercicio 8: Mi tiempo de pantalla")
print("\n******************** TIEMPO DE PANTALLA ********************")

#Damos de alta la variable app y las horas que paso al día
app = "Instagram"
horas_diarias = 2
print(f"\nPaso {horas_diarias} horas diarias en {app}")


#Calculamos las horas al año, esta formula dice: horas_anio = 4 * 365
horas_anio = horas_diarias * 365
print(f"Al año son {horas_anio} horas")


#Convertimos las horas a días completos (1 día tiene 24 horas)
#Esta formula dice: dias_anio = 1460 / 24, que da 60.833333
dias_anio = horas_anio / 24

#El :.1f muestra solo 1 decimal, así que se ve 60.8
print(f"¡Eso equivale a {dias_anio:.1f} días completos sin parar!")


#Calculamos cuántos meses son (un mes tiene aprox. 30 días)
#Esta formula dice: meses = 60.8 / 30
meses = dias_anio / 30

print(f"\nO sea, casi {meses:.1f} meses de mi año se van en {app}\n")
print("************************************************************")