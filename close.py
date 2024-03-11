from load import datatemp

def close():
    file = open('data.txt', 'a')
    for i in range(len(datatemp)):
        for j in range(len(datatemp[i])):
            if j == 0:
                file.write("- Nombre: " + str(datatemp[i][j]) + ' ||')
            elif j == 1:
                file.write(" - Apellido: " + str(datatemp[i][j]) + ' ||')
            elif j == 2:
                file.write(" - Edad: " + str(datatemp[i][j]) + ' ||')
            elif j == 3:
                file.write(" - DNI: " + str(datatemp[i][j]) + ' ||' + '\n')
    file.close()