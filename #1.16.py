#1.16
tur= int(input("""Ingrese el turno en que trabajo el operario:
1- Diurno 
2- Nocturno
"""))
Hor_tra=float(input("Ingrese la cantidad de horas trabajadas: "))
if tur==1:
    jornal_d=float(Hor_tra*35)
    print(f"El jornal del operario es: $ {jornal_d}")   
else:
    tur==2
    jornal_n=float(Hor_tra*40.6)
    print(f"El jornal del operario es: $ {jornal_n}") 
