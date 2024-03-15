import os
import msvcrt

def show(data):
    file = open('data.txt', 'r')
    contador = 0
    print('-------------------------')
    print('La lista de personas es: ')
    for i in data:
        contador += 1
        print('-------------------------')
        print(f'Persona', contador)
        print(f'- Nombre:', i.name)
        print(f'- Apellido:', i.surname)
        print(f'- Edad:', i.age)
        print(f'- DNI:', i.dni)
    print('-------------------------')
    print('Presione una tecla para continuar...')
    msvcrt.getch()
    os.system('cls')