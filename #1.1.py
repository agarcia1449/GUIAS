#1.1
# Pedir al usuario ingresar dos números
a = int(input("Ingrese un número, a = "))
b = int(input("Ingrese otro número, b = "))


# Realizar la división y calcular el resultado y el resto
resultado = a // b
resto = a % b


# Mostrar el resultado de la división y el resto
print("El resultado de a/b es = " + str(resultado))
print("El resto de a/b es = " + str(resto))