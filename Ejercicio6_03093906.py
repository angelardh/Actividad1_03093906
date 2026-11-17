print("Ejercicio 6: ¿Avisamos al cliente de un retraso?")
print("Nombre: Angela Delgado")
print("Matrícula: T03093906")
print()

# Preguntamos por los 4 problemas que pueden retrasar un embarque
barco = input("¿El barco llegó tarde? (si/no): ")
puerto = input("¿El puerto está saturado? (si/no): ")
documento = input("¿Falta algún documento? (si/no): ")
semaforo = input("¿Le tocó semáforo rojo en la aduana? (si/no): ")

# Convertimos cada respuesta en True o False
barco_tarde = barco == "si"
puerto_saturado = puerto == "si"
falta_documento = documento == "si"
semaforo_rojo = semaforo == "si"

# Contador de motivos de retraso
motivos = 0

print()
print("===== SEGUIMIENTO DEL EMBARQUE =====")

# or: con UN solo problema basta para avisar al cliente
if barco_tarde or puerto_saturado or falta_documento or semaforo_rojo:
    print("⚠️ Avisa al cliente: el embarque viene con retraso.")
    print("Motivos:")

    # Revisamos uno por uno cuál problema SÍ pasó
    if barco_tarde:
        print("  - El barco llegó tarde")
        motivos = motivos + 1
    if puerto_saturado:
        print("  - El puerto está saturado")
        motivos = motivos + 1
    if falta_documento:
        print("  - Falta un documento")
        motivos = motivos + 1
    if semaforo_rojo:
        print("  - Semáforo rojo en la aduana")
        motivos = motivos + 1

    print("Total de motivos:", motivos)
else:
    print("✅ El embarque va a tiempo. No hay que avisar al cliente.")

# La entrega normal tarda 10 días y cada motivo agrega 2 días
dias = 10 + motivos * 2
print("Días estimados de entrega:", dias)