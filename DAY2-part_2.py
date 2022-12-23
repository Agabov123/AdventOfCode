with open('day2part1.txt', 'r') as file:
    list = []
    for i in file.read().split('\n'):
        list.append(i)

def get_points():
    score2 = 0

    for x in list:
        
        if x == 'A X':
            score2 += 3
        elif x == 'B X':
            score2 += 1
        elif x == 'C X':
            score2 += 2
        elif x == 'A Y':
            score2 += 4
        elif x == 'B Y':
            score2 += 5
        elif x == 'C Y':
            score2 += 6
        elif x == 'A Z':
            score2 += 8
        elif x == 'B Z':
            score2 += 9
        elif x == 'C Z':
            score2 += 7 
    print(score2)
get_points()
