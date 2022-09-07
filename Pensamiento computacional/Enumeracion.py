objetivo = int(input('Escoge un entero: '))
respuesta = 0 

while respuesta**3 < objetivo:
    respuesta += 1

if respuesta**3 == objetivo:
    print(f'la raiz cubica de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene una raiz cubica exacta')
