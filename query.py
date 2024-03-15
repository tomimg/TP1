from factory import Human
def select():
    data: list = []
    with open('data.txt', 'r') as file:
        for i in file:
            parte = i.strip().split(',')
            person = Human(parte[0], parte[1], int(parte[2]), int(parte[3]))
            data.append(person)
    return data