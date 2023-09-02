#1.8
numero=input("Qué tabla del 1 al 10 desea ver?: ")
print("Esta es la tabla del " + (numero) )  
   
for i in range(1,11):
    resultado= i*int(numero)
    print (f"{numero}x{i}={resultado}")
