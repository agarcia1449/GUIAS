#1.7
# Pedir al usuario la cantidad de números de la sucesión de Fibonacci a mostrar
cantidad_numeros = int(input("Ingrese la cantidad de números de la sucesión de Fibonacci a mostrar: "))
c=0
#Inicializar los primeros dos términos de la sucesión
a, b = 0, 1
# Mostrar la sucesión de Fibonacci
print("Sucesión de Fibonacci:")
print(a)  
print(b)  
while cantidad_numeros > c:
    suc_fibo=a+b
    print(suc_fibo)
    a=b
    b=suc_fibo
    c +=1    
#otra forma de resolver
#for i in range(cantidad_numeros):
  #  print(a, end ="-")
  #  a, b = b, a + b