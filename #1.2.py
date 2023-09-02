#1.2
# Pedir al usuario ingresar dos números
a = int(input("Ingrese un número, a = "))
b = int(input("Ingrese otro número, b = "))
# Calcular ambos resultados
resultado_a = (a + b) ** 2
resultado_b = a ** 2 + (2 * (b * a)) + b ** 2
# Mostrar los resultados
print("El resultado de (a+b)**2 = " + str(resultado_a))
print("a**2 + (2*(b*a)) + b**2 = " + str(resultado_b))
# Comprobar la propiedad de los binomios al cuadrado
if resultado_a == resultado_b:
    print("Podemos afirmar entonces que Un binomio al cuadrado (suma) es igual al cuadrado del primer término, más el doble producto del primero por el segundo más el cuadrado del segundo.")
else:
    print("La propiedad de los binomios al cuadrado no se cumple para los números ingresados.")
