#1.14
num1=int(input("Ingrese un número: "))
num2=int(input("nuevamente, ingrese otro número: "))
num3=int(input("por último, Ingrese otro número: "))
suma=num1+num2+num3
if suma > 10:
    result=suma//2
    print(f"Como el resultado de la suma es mayor a 10, se dividio la suma en 2, el resultado es: {result}")   
else:
    suma < 10
    result=suma**3
    print(f"Como el resultado de la suma es menor a 10, se elevó la suma al cubo, el resultado es: {result}")
