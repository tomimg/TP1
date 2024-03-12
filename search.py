from load import datatemp
import os
import msvcrt

def search():
    print('-------------------------')
    print('Bienvenido a la busqueda de personas!')
    print('-------------------------')
    eleccion = input(str('Ingrese d para realizar busqueda por DNI o n para realizar busqueda por nombre: '))
    if eleccion.lower() == 'd':
        os.system('cls')
        print('-------------------------')
        print('Acabas de ingresar a la busqueda por DNI!')
        dni = int(input('Ingrese el DNI de la persona que desea buscar: '))
        with open('data.txt', 'r') as fp:
            for line in enumerate(fp):
                if str(dni) in line:
                    print('-------------------------')
                    print('Hemos encontrado a tu persona:')
                    print('-------------------------')
                    print(line)
                    print('-------------------------')
                    print('Presione una tecla para continuar...')
                    msvcrt.getch()
                    os.system('cls')
        fp.close()
        for i in datatemp:
            if str(dni) == i[3]:
                print('-------------------------')
                print('Hemos encontrado a tu persona:')
                print('-------------------------')
                print('- Nombre:', i[0])
                print('- Apellido:', i[1])
                print('- Edad:', i[2])
                print('- DNI:', i[3])
                print('-------------------------')
                print('Presione una tecla para continuar...')
                msvcrt.getch()
                os.system('cls')
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
        with open('data.txt', 'r') as file:
            for line in enumerate(file):
                if nombre.lower() in line:
                    print('-------------------------')
                    print('Hemos encontrado a tu persona:')
                    print('-------------------------')
                    print(line)
                    print('-------------------------')
                    print('Presione una tecla para continuar...')
                    msvcrt.getch()
                    os.system('cls')
        file.close()
        for i in datatemp:
            if nombre.lower() == i[0]:
                print('-------------------------')
                print('Hemos encontrado a tu persona:')
                print('-------------------------')
                print('- Nombre:', i[0])
                print('- Apellido:', i[1])
                print('- Edad:', i[2])
                print('- DNI:', i[3])
                print('-------------------------')
                print('Presione una tecla para continuar...')
                msvcrt.getch()
                os.system('cls')
        print('No hemos encontrado a una persona con ese nombre.')
        print('-------------------------')
        print('Presione una tecla para continuar...')
        msvcrt.getch()
        os.system('cls')