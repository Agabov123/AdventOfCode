with open('day6part1.txt', 'r') as file:
    list = []
    for i in file.read().split('\n'):
        for letter in i:
            list.append(letter)
            

def marker_position():
    count = 0
    while count < len(list):
        values = set(list[count:count+4])  # set does not have repeating values, so if the length of set is still 4 that means that it is the marker
        if len(values) == 4:
            print(values)
            print(count+4)
            break # function breaks after the first marker
        count += 1
marker_position()
