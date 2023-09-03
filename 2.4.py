#2.4
#Se importa MODULO RAMDOM para utilizar (random.randint)
import random
#Se le pide al usuario que ingrese cantidad de numeros que desea transformar
n=int(input("Ingrese la cantidad de veces que desea que el programa repita la accion: "))

#Generar n números aleatorios entre el rango de 5000 y 450000,
for i in range(n):
 numero_dec_aleatorio = random.randint(5000,450000)
 
 # Se utiliza la FUNCION HEX() para pasar los numero aleatorios a formato hexadecimal 
 numero_exa=hex(numero_dec_aleatorio)

#mostrar y generar el numero hexadecimal
 print(f"Decimal {numero_dec_aleatorio} = {numero_exa} Hexadecimal")