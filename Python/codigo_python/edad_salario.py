#Algoritmo que pida edad salario y diga si necesita declarar renta.
edad = int(input("Indique su edad: "))
salario = int(input("Ingrese su salario mensual: "))
if edad >= 18 and salario >= 1500000:
    print("Perdiste!, te toca declarar renta bro, suete 😁")
else:
    print("Aun no te toca pagar plata a la dian bro, felicidades 😁")
