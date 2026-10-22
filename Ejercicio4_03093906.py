print("\n+++++++++++++")
print("Ejercicio realizado por Angela\n")
print("Ejercicio 4: ¿Cuánto tardo en terminar una serie?")

# Damos de alta las variables
serie = "The Mermaid Tale"
temporadas = 6
episodios_por_temporada = 10
minutos_por_episodio = 45
horas_al_dia = 1  # cuánto tiempo le dedico diario
# Usamos las variables en las fórmulas
# Total de episodios
total_episodios = temporadas * episodios_por_temporada

# Total de minutos y horas
total_minutos = total_episodios * minutos_por_episodio
total_horas = total_minutos / 60

# ¿Cuántos días necesito?
dias_necesarios = total_horas / horas_al_dia

print("\nResultados")
print(f"{serie} tiene {total_episodios} episodios")
print(f"Son {total_minutos} minutos en total")
print(f"Equivale a {total_horas:.1f} horas")
print(f"Viendo {horas_al_dia} horas diarias, la terminas en {dias_necesarios:.1f} días")
print("\n♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥")