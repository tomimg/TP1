import os
import msvcrt
from load import load
from show import show
from close import close
from search import search
from query import select
from modify import modify
from remove import delete
data: list[str] = select()

def modify_or_delete(data):
    print('-------------------------')
    print('- Seleccione una opción: ')
    print('1. Modificar')
    print('2. Eliminar')
    print('-------------------------')

    eleccion = input('Seleccione una opción (1-2): ')

    if eleccion == '1':
        modify(data)
    elif eleccion == '2':
        delete(data)
    else:
        print('Opción inválida.')

    print('-------------------------')
    print('Presione una tecla para continuar...')
    msvcrt.getch()
    os.system('cls')

def menu():
    while True:
        print('-------------------------')
        print('Bienvenido, seleccione una opción:')
        print('1. Cargar')
        print('2. Mostrar')
        print('3. Buscar')
        print('4. Modificar/Eliminar')
        print('5. Salir')
        print('-------------------------')

        eleccion = (input('Seleccione una opción (1-5): '))

        if eleccion == '1':
            os.system('cls')
            load(data)
        elif eleccion == '2':
            os.system('cls')
            show(data)
        elif eleccion == '3':
            os.system('cls')
            search(data)
        elif eleccion == '4':
            os.system('cls')
            modify_or_delete(data)
        elif eleccion == '5':
            close(data)
            print('Guardado con éxito. \n Saliendo del programa...')
            os.system('cls')
            break