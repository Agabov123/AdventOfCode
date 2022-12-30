with open('day7part1.txt', 'r') as file:
    list = []
    for i in file.read().split('\n'):
        for letter in i:
            list.append(letter)
            