print("Ejercicio 5: Cálculo de impuestos con el T-MEC")
print("Nombre: Angela Delgado")
print("Matrícula: 03093906")
print()

# Pedimos los datos de la mercancía
pais = input("País de origen en MAYÚSCULAS y sin acento (MEXICO, ESTADOS UNIDOS, CANADA, CHINA...): ")
certificado = input("¿Tienes certificado de origen? (si/no): ")
valor = float(input("Valor de la mercancía en dólares: "))

# 1. Convierte la respuesta del certificado en True o False
tiene_certificado = certificado == "si"

print()
print("===== CÁLCULO DE IMPUESTOS DE IMPORTACIÓN =====")

# 2. Si el país es MEXICO, la mercancía es nacional y no se importa
if pais == "MEXICO":
    print("🇲🇽 Es mercancía nacional. No paga impuestos de importación.")
else:
    # 3. Escribe la condición del T-MEC: el país es ESTADOS UNIDOS o CANADA,
    #    y además tiene certificado. ¡No olvides los paréntesis!
    if (pais == "ESTADOS UNIDOS" or pais == "CANADA") and tiene_certificado:
        # 4. ¿Cuánto arancel se cobra si SÍ aplica el T-MEC?
        arancel = 0
        print("✅ Aplica el trato preferencial del T-MEC.")
    else:
        # 5. ¿Cuánto arancel se cobra si NO aplica?
        arancel = 15
        print("❌ No aplica el trato preferencial. Se cobra el arancel general.")

    # 6. Calcula el impuesto del arancel
    impuesto_arancel = valor * arancel / 100

    # 7. El IVA es el 16% de (valor + impuesto del arancel)
    iva = (valor + impuesto_arancel) * 16 / 100

    # 8. El total es el valor + impuesto del arancel + IVA
    total = valor + impuesto_arancel + iva

    print("Arancel: ", arancel, "%", sep="")
    print("Impuesto del arancel: $", impuesto_arancel, sep="")
    print("IVA: $", iva, sep="")
    print("Total a pagar: $", total, sep="")

    # 9. Aviso de ahorro: viene de ESTADOS UNIDOS o CANADA, pero NO tiene certificado
    if (pais == "ESTADOS UNIDOS" or pais == "CANADA") and not tiene_certificado:
        ahorro = valor * 15 / 100
        print("💡 Con certificado de origen te habrías ahorrado en arancel: $", ahorro, sep="")