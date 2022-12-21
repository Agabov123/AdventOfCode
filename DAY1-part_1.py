def get_highest(f):
    with open(f, 'r') as file:
        list = []
        for i in file.read().split('\n'):
            list.append(i)
        
    highest = 0
    total_calories = 0
    count = 0
    for i in list:
        if i != '':
            total_calories += int(i)
        else:
            count += 1
            if total_calories > highest:
                highest = total_calories
            total_calories = 0
    print(count, highest)
get_highest('day1part1.txt')