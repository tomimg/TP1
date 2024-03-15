from factory import Human

def find_by_name(data, name):
    for person in data:
        if person.name == name:
            return person
    return None

def modify(data):
    print('-------------------------')
    name = input("Ingrese el nombre de la persona que desea modificar: ").strip().lower()
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
        new_name = input('- Nuevo nombre: ').strip().lower()
        new_surname = input('- Nuevo apellido: ').strip().lower()
        new_age = int(input('- Nueva edad: '))
        new_dni = int(input('- Nuevo DNI: '))
        person.name = new_name
        person.surname = new_surname
        person.age = new_age
        person.dni = new_dni
        print("Persona modificada.")
    else:
        print("Persona no encontrada.")