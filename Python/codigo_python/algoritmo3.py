#algoritmo que permita mostrar el precio de un ticket a una sala de videojuegos, si la persona tiene una edad entre 5-10 años el precio es 5k si la edad esta por encima de 10-15 el ticket cuesta 10k, y si es mayor de 15 cuesta 15k.
edad = int(input("Bienvenido a la sala de video juegos cuc, Indicanos tu edad por favor: "))
if edad <= 10:
    print("El precio del ticket es de 5k")
elif edad <= 15:
    print("El precio del ticket es de 10")
else:
    print("El precio del ticket es de 15k")

    