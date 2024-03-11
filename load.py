import os
datatemp = []
def load():
    persona = []
    print('-------------------------')
    print('Bienvenido a la carga de datos!')
    persona.append(str(input('- Ingresa el nombre de la persona: ')))
    persona.append(str(input('- Ingrese el apellido de la persona: ')))
    persona.append(str(input('- Ingrese la edad de la persona: ')))
    persona.append(str(input('- Ingrese el DNI de la persona: ')))
    print('-------------------------')
    datatemp.append(persona)
    os.system('cls')
    return datatemp