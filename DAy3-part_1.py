with open('day3part1.txt', 'r') as file:
    list = []
    for i in file.read().split('\n'):
        list.append(i)

def get_score():
    list_type = []
    list_values = []
    for i in list:
        part1 = i[:len(i)//2]
        part2 = i[len(i)//2:]
        common = set(part1).intersection(part2).pop()
        common = str(common)
        list_type.append(common)
        if common.isupper():
            list_values.append(ord(common) - ord('A') + 27)
        elif common.islower():
            list_values.append(ord(common) - ord('a') + 1)
    print(len(list_type))
    print(sum(list_values))
            
get_score()
