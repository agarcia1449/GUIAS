#1.9
#Pedir al usuario que ingrese dos numeros
num_1=int(input("Ingrese el dividendo:"))
num_2=int(input("Ingrese el divisor:"))
#realizar la division y el resto
resultado=num_1//num_2
resto=num_1%num_2
#Mostrar en pantalla los resultados (division y resto)
print(f"{num_1}:{num_2}={resultado}")
print("El resto de la division es= "+str(resto))
