import os
import msvcrt
def delete(data):
    print('-------------------------')
    while True:
        dni = input('Ingrese el DNI de la persona que desea eliminar: ').strip()
        if dni == '':
            print('-------------------------')
            print('Pone un DNI en condiciones!')
            print('-------------------------')
        elif dni.isdigit() and int(dni) >= 0:
            break
        else:
            print('-------------------------')
            print('Pone un DNI en condiciones!')
            print('-------------------------')
    for person in data:
        if int(person.dni) == int(dni):
            data.remove(person)
            print(f'Persona con DNI {dni} eliminada.')
            return
    print('Persona no encontrada.')
    print('-------------------------')
    print('Presione una tecla para continuar...')
    msvcrt.getch()
    os.system('cls')

