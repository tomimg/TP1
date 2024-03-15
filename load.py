from factory import Human
import os
def load(data):
    print('-------------------------')
    print('Bienvenido a la carga de datos!')
    while True:
        name = str(input('Ingrese el nombre de la persona: ')).strip().lower()
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
    while True:
        surname = str(input('Ingrese el apellido de la persona: ')).strip().lower()
        if surname == '':
            print('-------------------------')
            print('Ingresa un apellido en condiciones!')
            print('-------------------------')
        elif not surname.isalnum():
            print('-------------------------')
            print('Pone un apellido en condiciones!')
            print('-------------------------')

        else: 
            break
    while True:
        age = input('Ingrese la edad de la persona: ').strip()
        if age == '':
            print('-------------------------')
            print('Pone una edad en condiciones!')
            print('-------------------------')
        elif age.isdigit() and int(age) >= 0:
            break
        else:
            print('-------------------------')
            print('Pone una edad en condiciones!')
            print('-------------------------')
    while True:
        dni = input('Ingrese el DNI de la persona: ').strip()
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
    
    print('-------------------------')
    person = Human(name, surname, age, dni)
    data.append(person)
    os.system('cls')
    return data