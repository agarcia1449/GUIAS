#2.3
# variables
suel_max=float("-inf")
sueldo_min=float("inf")
mes_sueldo_max = None
mes_sueldo_min = None
sum=0

#Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año
for i in range(1 , 7 ):
    mes=float(input(f"Ingrese el sueldo de correspondiente al mes {i}: "))
    
    if mes>suel_max:
        suel_max=mes
        mes_sueldo_max =(i)
        
    if mes<sueldo_min:
       sueldo_min=mes
       mes_sueldo_min =(i)

    sum += mes

#Calcula en qué mes recibió el sueldo más bajo del período.
print (f"Sueldo minimo ganado es: {sueldo_min} correspondiente al mes {mes_sueldo_min}")  

#Calcula en qué mes recibió el sueldo más alto del período  
print (f"Sueldo maximo ganado es: {suel_max} correspondiente al mes {mes_sueldo_max}")  
# Calcula AGUINALDO
aguinaldo=suel_max/2
print(f"SAC= ${aguinaldo}")

#Calcula sueldo promedio del semestre.
#(SUMAR SUELDOS  / 6)
promedio=sum/6
print (f"SUELDO PROMEDIO= ${promedio}") 
