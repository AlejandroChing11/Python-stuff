#algoritmo que pida 3 numeros diga cual es el mayor y cual es el menor.
num1 = int(input("Dame el valor del numero 1 por favor: "))
num2 = int(input("Dame el valor del numero 2 por favor: "))
num3 = int(input("Dame el valor del numero 3: "))

if num1 > num2 and num1 > num3:
    print("El numero mayor es", num1)
elif num2 > num3 and num2 > num1:
    print("El numero mayor es", num2)
elif num3 > num2 and num3 > num1:
    print("El numero mayor es", num3)
if num1 < num2 and num1 < num3:
    print("El numero menor es", num1)
elif num2 < num3 and num2 < num1:
    print("El numero menor es", num2)
elif num3 < num2 and num3 < num1:
    print("El numero menor es", num3)
if num1 > num2 and num2 < num3:
    print("El numero del medio es", num3)
elif num2 > num3 and num3 < num1:
    print("El numero del medio es", num1)
elif num1 < num2 and num2 < num3:
    print("El numero del medio es", num2)
else: 
    print("Los numeros son iguales")


