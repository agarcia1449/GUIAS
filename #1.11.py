#1.11
#Pide al usuario que ingrese mes a mes el sueldo
ENE=int(input("Ingrese el sueldo neto del mes de enero: "))
FEB=int(input("Ingrese el sueldo neto del mes de febrero: "))
MAR=int(input("Ingrese el sueldo neto del mes de marzo: "))
ABR=int(input("Ingrese el sueldo neto del mes de abril: "))
MAY=int(input("Ingrese el sueldo neto del mes de mayo: "))
JUN=int(input("Ingrese el sueldo neto del mes de junio: "))
JUL=int(input("Ingrese el sueldo neto del mes de julio: "))
AGO=int(input("Ingrese el sueldo neto del mes de agosto: "))
SEP=int(input("Ingrese el sueldo neto del mes de septiembre: "))
OCT=int(input("Ingrese el sueldo neto del mes de octubre: "))
NOV=int(input("Ingrese el sueldo neto del mes de noviembre: "))
DIC=int(input("Ingrese el sueldo neto del mes de diciembre: "))


#calcula el 10% del la suma de todos los sueldos netos
aho_anual=(ENE+FEB+MAR+ABR+MAY+JUN+JUL+AGO+SEP+OCT+NOV+DIC)*0.1


#imprime el ahorro anual
print ("Su ahorro anual es: $ " + str(aho_anual))
