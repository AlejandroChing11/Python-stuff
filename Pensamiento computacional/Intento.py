objetivo = int(input('Elige un numero: '))
print(f'¿Por cual metodo te gustaria encontrar la raiz cuadrada de {objetivo}')
print('1. Enumeracion exhaustiva')
print('2. Aproximación')
print('3. Busqueda Binaria')
opcion = int(input(f'¿Por cual metodo deseas hacer el proceso?: '))


def enumeracion_exhaustiva(objetivo):
    objetivo = int(input('Escoge un entero: '))
respuesta = 0 

while respuesta**2 < objetivo:
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'la raiz cubica de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene una raiz cubica exacta')


def aproximacion(objetivo):
    objetivo = int(input('Escoge un numero: '))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada de {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')


    
def busquedabinaria_binaria(objetivo):
    objetivo = int(input('Escoge un numero: '))
epsilon = 0.001
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta

    respuesta = (alto + bajo) / 2

print(f'La raiz cuadrada del {objetivo} es {respuesta} ')


