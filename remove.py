def delete(data):
    name = input('- Ingrese el nombre de la persona que desea eliminar: ')
    for person in data:
        if person.name == name:
            data.remove(person)
            print(f'Persona {name} eliminada.')
            return
    print('Persona no encontrada.')
