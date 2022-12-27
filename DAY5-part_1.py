with open('day5part1.txt', 'r') as file:
    list = []
    for i in file.readlines():
        action = []
        for x in i.strip().split(' '):
            action.append(x)
        list.append(action)

containers = [['Q','S','W','C','Z','V','F','T'], ['Q','R','B'], ['B','Z','T','Q','P','M','S'], ['D','V','F','R','Q','H'], ['J','G','L','D','B','S','T','P'], ['W','R','T','Z'], ['H','Q','M','N','S','F','R','J'], ['R','N','F','H','W'], ['J','Z','T','Q','P','R','B']]

def solution():
    for i in list:
        print(i)
        movefrom = int(i[3])-1
        moveto = int(i[5])-1
        for x in range(int(i[1])):
            l = containers[movefrom][-1]
            del(containers[movefrom][-1])
            containers[moveto].append(l)
            print(l)
        
    solution = ''
    for container in containers:
        solution += container[-1]
    print(solution)
solution()