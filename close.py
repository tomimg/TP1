from factory import Human
def close(data):
    file = open('data.txt', 'w')
    for human in data:
        file.write(f'{human.name},{human.surname},{human.age},{human.dni}\n')
    file.close()