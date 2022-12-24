with open('day4part1.txt', 'r') as file:
    list = []
    for i in file.read().split('\n'):
        list.append(i)
def get_number ():
    count = 0
    for i in list:
        tasks = i.split(',')
        task1 = tasks[0].split('-')
        task2 = tasks[1].split('-')
        sections1 = []
        sections2 = []
        for j in range(int(task1[0]), int(task1[1])+1):
            sections1.append(j)
        for y in range(int(task2[0]), int(task2[1])+1):
            sections2.append(y)
        if all(item in sections1 for item in sections2) or all(item in sections2 for item in sections1):
            count += 1
 

    print(count)
get_number()