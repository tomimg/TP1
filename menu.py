import os
from load import load
from show import show
from close import close
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
            load()
        elif eleccion == '2':
            os.system('cls')
            show()
        elif eleccion == '5':
            close()
            print('Guardado con éxito. \n Saliendo del programa...')
            os.system('cls')
            break