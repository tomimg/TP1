import os
import msvcrt
bandera = False

def search(data):
    global bandera
    
    print('-------------------------')
    print('Bienvenido a la busqueda de personas!')
    print('-------------------------')
    eleccion = input(str('Ingrese d para realizar busqueda por DNI o n para realizar busqueda por nombre: '))
    if eleccion.lower() == 'd':
        os.system('cls')
        print('-------------------------')
        print('Acabas de ingresar a la busqueda por DNI!')
        dni = int(input('Ingrese el DNI de la persona que desea buscar: '))
        for i, human in enumerate(data):
            if human.dni == int(dni):
                print('-------------------------')
                print('Hemos encontrado a tu persona:')
                print('-------------------------')
                print('- Nombre:', human.name)
                print('- Apellido:', human.surname)
                print('- Edad:', human.age)
                print('- DNI:', human.dni)
                print('-------------------------')
                print('Presione una tecla para continuar...')
                msvcrt.getch()
                os.system('cls')
                bandera = True
        if not bandera:
            print('No hemos encontrado a una persona con ese DNI.')
            print('-------------------------')
            print('Presione una tecla para continuar...')
            msvcrt.getch()
            os.system('cls')
    else:
        os.system('cls')
        print('-------------------------')
        print('Acabas de ingresar a la busqueda por nombre!')
        nombre = str(input('Ingrese el nombre de la persona que desea buscar: '))
        for i, human in enumerate(data):
            if human.name.lower() == nombre.lower():
                print('-------------------------')
                print('Hemos encontrado a:')
                print('-------------------------')
                print('- Nombre:', human.name)
                print('- Apellido:', human.surname)
                print('- Edad:', human.age)
                print('- DNI:', human.dni)
                print('-------------------------')
                print('Presione una tecla para continuar...')
                msvcrt.getch()
                os.system('cls')
                bandera = True
        if not bandera:
            print('No hemos encontrado a una persona con ese nombre.')
            print('-------------------------')
            print('Presione una tecla para continuar...')
            msvcrt.getch()
            os.system('cls')