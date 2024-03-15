from factory import Human
import os
import msvcrt
def find_by_name(data, name):
    for person in data:
        if person.name == name:
            return person
    print('Persona no encontrada.')
    print('-------------------------')
    print('Presione una tecla para continuar...')
    msvcrt.getch()
    os.system('cls')


def modify(data):
    print('-------------------------')
    while True:
        name = str(input('Ingrese el nombre de la persona que desea modificar: ')).strip().lower()
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
    person = find_by_name(data, name)
    if person is not None:
        print('-------------------------')
        print("Persona encontrada:")
        print('-------------------------')
        print(f'- Nombre:', person.name)
        print(f'- Apellido:', person.surname)
        print(f'- Edad:', person.age)
        print(f'- DNI:', person.dni)
        print('-------------------------')
        while True:
            new_name = str(input('Ingrese el nuevo nombre de la persona: ')).strip().lower()
            if new_name == '':
                print('-------------------------')
                print('Ingresa un nombre en condiciones!')
                print('-------------------------')
            elif not new_name.isalnum():
                print('-------------------------')
                print('Pone un nombre en condiciones!')
                print('-------------------------')
            else: 
                break
        while True:
            new_surname = str(input('Ingrese el nuevo apellido de la persona: ')).strip().lower()
            if new_surname == '':
                print('-------------------------')
                print('Ingresa un apellido en condiciones!')
                print('-------------------------')
            elif not new_surname.isalnum():
                print('-------------------------')
                print('Pone un apellido en condiciones!')
                print('-------------------------')

            else: 
                break
        while True:
            new_age = input('Ingrese la nueva edad de la persona: ').strip()
            if new_age == '':
                print('-------------------------')
                print('Pone una edad en condiciones!')
                print('-------------------------')
            elif new_age.isdigit() and int(new_age) >= 0:
                break
            else:
                print('-------------------------')
                print('Pone una edad en condiciones!')
                print('-------------------------')
        while True:
            new_dni = input('Ingrese el nuevo DNI de la persona: ').strip()
            if new_dni == '':
                print('-------------------------')
                print('Pone un DNI en condiciones!')
                print('-------------------------')
            elif new_dni.isdigit() and int(new_dni) >= 0:
                break
            else:
                print('-------------------------')
                print('Pone una edad en condiciones!')
                print('-------------------------')
        person.name = new_name
        person.surname = new_surname
        person.age = new_age
        person.dni = new_dni
        print("Persona modificada.")
    else:
        print("Persona no encontrada.")