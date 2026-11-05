print("Ejercicio 1: Inicia sesión en Roblox")
print("Nombre: Angela Delgado")
print("Matrícula: t03093906")
print()

# Guardamos el usuario y la contraseña correctos
usuario_correcto = "delg_angela"
contrasena_correcta = "roblox123"

# Al inicio todavía NO ha iniciado sesión
sesion_iniciada = False

# Mientras NO haya iniciado sesión, se repite
while sesion_iniciada == False:
    # Pedimos el usuario y la contraseña
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    # ¿El usuario es IGUAL al correcto?
    if usuario == usuario_correcto:
        # Sí existe. Ahora: ¿la contraseña es IGUAL a la correcta?
        if contrasena == contrasena_correcta:
            print("✅ ¡Bienvenido,", usuario, "!")
            # Ya entró: esto hace que el while se detenga
            sesion_iniciada = True
        else:
            print("❌ La contraseña es incorrecta")
    else:
        print("❌ Ese usuario no existe")

# Esto se ejecuta cuando ya salió del while
print("🎮 Cargando tus juegos...")