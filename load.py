from factory import Human
import os
def load(data):
    print('-------------------------')
    print('Bienvenido a la carga de datos!')
    name = (str(input('- Ingresa el nombre de la persona: '))).strip().lower()
    surname = (str(input('- Ingrese el apellido de la persona: '))).strip().lower()
    age = (int(input('- Ingrese la edad de la persona: ')))
    dni = (int(input('- Ingrese el DNI de la persona: ')))
    print('-------------------------')
    person = Human(name, surname, age, dni)
    data.append(person)
    os.system('cls')
    return data