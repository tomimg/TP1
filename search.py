import os
import msvcrt
bandera = False

def search(data):
    global bandera
    
    print('-------------------------')
    print('Bienvenido a la busqueda de personas!')
    print('-------------------------')
    while True:
        eleccion = input('Ingrese "D" para realizar busqueda por DNI o "N" para realizar busqueda por nombre: ').upper().strip()
        if eleccion == 'D' or eleccion == 'N':
            break
        else:
            print('Pone un D o N crack!')
    if eleccion.lower() == 'd':
        os.system('cls')
        print('-------------------------')
        print('Acabas de ingresar a la busqueda por DNI!')
        while True:
            dni = input('Ingrese el DNI de la persona que desea buscar: ').strip()
            if dni == '':
                print('Pone un DNI en condiciones!')
            elif dni.isdigit() and int(dni) >= 0:
                break
            else:
                print('Pone un DNI en condiciones!')
        for i, human in enumerate(data):
            if int(human.dni) == int(dni):
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
        while True:
            nombre = str(input('Ingrese el nombre de la persona que desea buscar: ')).strip()
            if nombre == '':
                print('Ingresa un nombre en condiciones!')
            elif not nombre.isalnum():
                print('Pone un nombre en condiciones!')
            else: 
                break
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