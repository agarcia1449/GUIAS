#1.10
# Pedir al usuario que elija una operación
operacion = int(input("""Qué operación desea realizar, elija una opción:
                1: CONVERTIR DE USD a $
                2: CONVERTIR DE $ a USD
                """))
# Realizar operación según la elección del usuario
if operacion == 1:
    val_dol = int(input("Ingrese el valor del dólar hoy: "))
    dol_cant = int(input("Ingrese la cantidad de dólares a convertir: "))
    resultado_1 = val_dol * dol_cant
    print(f"USD {dol_cant} equivalen a: $ {resultado_1}")
elif operacion == 2:
    val_dol = int(input("Ingrese el valor del dólar hoy: "))
    pes_cant = int(input("Ingrese la cantidad de pesos a convertir: "))
    resultado_2 = pes_cant / val_dol
    print(f"$ {pes_cant} equivalen a: USD {resultado_2}")  
else:
    print("Ingresaste una opción inválida.")
