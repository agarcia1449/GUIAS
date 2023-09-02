#1.12
elec=int(input("""Que desea convertir a cm.?
               1-pies a cm.
               2-pulgadas a cm.
               """))


if elec ==1:
    conv_p=float(input("Ingrese la cantidad de pies que desea convertir: "))
    resul_1=float(conv_p*30.48)
    print(f"{conv_p} pie/s a cm= {resul_1} cm.")
   
elif elec ==2:
    conv_pul=float(input("Ingrese la cantidad de pulgadas que desea convertir: "))
    resul_2=float(conv_pul*2.54)
    print(f"{conv_pul} pulgada/s a cm= {resul_2} cm.")
   
else:
    print("Ingresó una opción incorrecta")
