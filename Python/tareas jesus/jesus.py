#Programa que permita calcular area de un triangulo.

def area_triangulo(base, altura):
    return (base * altura) // 2


base = int(input("Ingrese la medida de la base por favor: "))
altura = int(input("Ingrese la medida de la altura por favor: "))

area = area_triangulo(base, altura)

print("El Area del triangulo es igual a: ", area)


    



