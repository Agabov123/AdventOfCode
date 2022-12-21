def get_highest(f):
    with open(f, 'r') as file:
        list = []
        for i in file.read().split('\n'):
            list.append(i)
        
    highest = 0
    total_calories = 0
    count = 0
    list_total = []
    top3 = 0
    for i in list:
        if i != '':
            total_calories += int(i)
        else:
            count += 1
            list_total.append(total_calories)
            if total_calories > highest:
                highest = total_calories
            total_calories = 0
    list_total.sort(reverse=True)
    for i in list_total[:3]:   
        top3 += i
        print(i)

    print(top3)
get_highest('day1part1.txt')