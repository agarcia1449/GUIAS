#2.1
import time
#Pedir al usuario la cantidad de competidores y corroborar que sea numero lo que ingreso
while True:
    n=(input("Ingrese la cantidad de competidores: "))
    if n.isdigit(): 
        break
    else:
        print("Ingrese un numero por favor.")
        
#Iniciamos Variables para ganador, record, promedio, tiempo total y tiempo ganador
ganador = ""
record = 0
promedio = float(0)
tiempo_total=float(0)
tiempo_ganador = 0
empate=int(0)

for i in range(1, int(n)+ 1):
    nombre=input(f"Ingrese el nombre del competidor {i}: ")
    tiempo=float(input(f'Ingrese el tiempo de {nombre} (en segundos): '))
      
#Se comprueba si hay empate en el saso de ser dos jugadores, si no hay empate, quien es el ganador
    if int(n)==2 and tiempo==tiempo_ganador:
        print ("Hay un empate")       
        print(f"el tiempo que tardaron fue: {tiempo_ganador}")
        empate=True
        #Verificamos si hay un nuevo record
        record=float(input("Ingrese el record actual (en segundos) para esta carrera: "))
        print("Por favor espera que chequeamos si hay nuevo record...")
        time.sleep(5)
        if record<tiempo_ganador:
            print(f"REALIZARON UN NUEVO RECORD!! FELICIDADES!")
        else:
            print("No hay un nuevo record para esta carrera.")

    elif tiempo>tiempo_ganador:
         ganador=nombre
         tiempo_ganador=tiempo 
    tiempo_total+=tiempo  

#Si no es empate
if not(empate):
    print(f"el tiempo total es: {tiempo_total}")
#Imprimimos quien es ganador
    print(f"el ganador es: {ganador}")

#Sacamos el promedio del tiempo: promedio=tiempo_total/int(n) y lo imprimimos
    promedio = tiempo_total/float(n)
    print(f"El promedio en tiempo de los competidores es: {promedio} segundos.")

#Verificamos si hay un nuevo record
    record=float(input("Ingrese el record actual (en segundos) para esta carrera: "))
    print("Por favor espera que chequeamos...")
    time.sleep(5)
    if record<tiempo_ganador:
        print(f"HAY UN NUEVO RECORD!!{ganador} FELICIDADES!")
    else:
        print("No hay un nuevo record para esta carrera.")
 