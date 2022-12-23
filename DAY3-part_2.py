with open('day3part1.txt', 'r') as file:
    list = []
    for i in file.read().split('\n'):
        list.append(i)

def get_score():
    list_type = []
    list_values = []
    counter = 0
    while counter < len(list):
        line1 = list[counter]
        counter += 1
        line2 = list[counter]
        counter += 1
        line3 = list[counter]
        counter += 1
        common = (set(line1).intersection(line2)).intersection(line3).pop()
        common = str(common)
        list_type.append(common)
        if common.isupper():
            list_values.append(ord(common) - ord('A') + 27)
        elif common.islower():
            list_values.append(ord(common) - ord('a') + 1)
    print(list_values)
    print(sum(list_values))
            
get_score()
