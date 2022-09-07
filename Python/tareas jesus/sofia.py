def calculadora_areatriangulo(base, altura):
    return (base * altura) // 2


altura = int(input("Ingrese valor de altura: "))
base = int(input("Ingrese valor base: "))

area = calculadora_areatriangulo(base, altura)

print("El valor del area es: ",area)
