def get_highest(f):
    with open(f, 'r') as file:
        list = []
        for i in file.read().split('\n'):
            list.append(i)
        
    
    print(list)
get_highest('day2part1.txt')