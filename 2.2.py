#2.2
#importar modulo time para time.sleep(1)
import time
#pedir al usuario que ingrese dos numeros para registrar los impares de ese rango
while True:
    num1,num2=(input("""Ingresa dos numeros enteros: 
                    *Separados por un espacio y de menor a mayor: 
                     """)).split()
#verificar que ambos sean numeros
    if num1.isdigit() and num2.isdigit():
        print(f"Usted eligio el siguiente rango {num1} a {num2}")
        break
    
    else:
        print("No ingresaste numeros enteros.")
        time.sleep(1)

#imprimir impares ascendente
print("Impares de tu rango de forma ascendente. ")
for i in range(int(num1), int(num2) + 1):
    if i%2 != 0:
        print(i)
print("Impares de tu rango de forma descendente.")    
#imprimir impares descendente
for i in range(int(num2), int(num1)- 1, -1):
    if i%2 != 0:
        print(i)