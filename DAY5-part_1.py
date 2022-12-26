with open('day5part1.txt', 'r') as f:
    list = f.readlines()
    list = [entry for entry in list]
def move():
    number_of_crates = len(list[0])//4
    crate_lines = list[:list.index('\n')-1]
    moving_lines = list[list.index('\n')+1:]
    print(number_of_crates, crate_lines, moving_lines)
    
move()