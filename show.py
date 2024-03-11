from load import datatemp

def show():
    file = open('data.txt', 'r')
    contador = 0
    for line in file.readlines():
        contador += 1
        print('-------------------------')
        print('Persona', contador)
        print(line)
    file.close()
    for i in datatemp:
        contador += 1
        print('-------------------------')
        print('Persona', contador)
        print('- Nombre:', i[0])
        print('- Apellido:', i[1])
        print('- Edad:', i[2])
        print('- DNI:', i[3])