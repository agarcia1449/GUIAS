 #1.13


nom = ""
ape = ""
dom = ""
while nom == "":
    nom=input("Ingrese su nombre: ")
while ape == "":
    ape=input("Ingrese su apellido: ")   
while dom == "":    
    dom=input("""Dominio:
      "ejemplo: gmail.com.ar"
        """)
if nom[0]!=ape[0]:
    print(f"Su mail es: {nom[0]}{ape}@{dom}")   
else:
    print(f"Su mail es: {nom}.{ape}@{dom}")