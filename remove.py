import os
import msvcrt
def delete(data):
    print('-------------------------')
    while True:
        name = str(input('Ingrese el nombre de la persona que desea eliminar: ')).strip().lower()
        if name == '':
            print('-------------------------')
            print('Ingresa un nombre en condiciones!')
            print('-------------------------')
        elif not name.isalnum():
            print('-------------------------')
            print('Pone un nombre en condiciones!')
            print('-------------------------')
        else: 
            break
    for person in data:
        if person.name == name:
            data.remove(person)
            print(f'Persona {name} eliminada.')
            return
    print('Persona no encontrada.')
    print('-------------------------')
    print('Presione una tecla para continuar...')
    msvcrt.getch()
    os.system('cls')

