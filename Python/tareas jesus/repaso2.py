#programa que verifique si la contraseña es segura

def verificador(contraseña):
    largo = False
    mayus = False
    nume = False
    if len(contraseña) > 8:
        largo = True
    for i in range(len(contraseña)):
        if contraseña[i].isupper():
            mayus = True
        if contraseña[i].isnumeric():
            nume = True
    if largo and mayus and nume:
        return True
    else:
        return False

contraseña = str(input("Ingrese la contraseña: "))
verificacion = verificador(contraseña)
if verificacion:
    print("TU contraseña es segura!")
else:
    print("Tu contraseña no es segura")



