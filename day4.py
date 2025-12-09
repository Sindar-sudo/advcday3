array = []
maxrolls = 4
accessibleroll = 1
totalroll = 0

with open("day4.txt") as file:
    for line in file:
        array.append(list(line.rstrip("\n")))

def too_many_rolls(array, row, col):
    rolls = 0
    length = len(array[row])
    height = len(array)
    #row -1 col 0 ok
    if row > 0 and (array[row-1][col] == '@' or array[row-1][col] == 'x'): 
        rolls += 1
    #row +1 col 0 ok
    if row < height -1 and (array[row+1][col] == '@' or array[row+1][col] == 'x'): 
        rolls += 1
    #row 0 col -1 ok
    if col > 0 and (array[row][col-1] == '@' or array[row][col-1] == 'x'): 
        rolls += 1
    #row 0 col +1 ok
    if col < length-1 and (array[row][col+1] == '@' or array[row][col+1] == 'x'): 
        rolls += 1
    #row +1 col -1 ok
    if row < height -1 and col > 0 and (array[row+1][col-1] == '@' or array[row+1][col-1] == 'x'): 
        rolls += 1
    #row -1 col +1 ok
    if row > 0 and col < length -1 and (array[row-1][col+1] == '@' or array[row-1][col+1] == 'x'): 
        rolls += 1
    #row -1 col -1 ok
    if row >0 and col > 0 and (array[row-1][col-1] == '@' or array[row-1][col-1] == 'x'): 
        rolls += 1
    #row +1 col +1 ok
    if row < height -1 and col < length -1 and (array[row+1][col+1] == '@' or array[row+1][col+1] == 'x'): 
        rolls += 1

    return rolls >= maxrolls


while accessibleroll != 0:
    accessibleroll = 0
    for r in range(len(array)):
        for c in range(len(array[r])):
            if array[r][c] == '@':
                if too_many_rolls(array, r, c):
                    print("Too many rolls at", r, c)
                else:
                    accessibleroll +=1
                    array[r][c] = 'x'
    #if too_many_rolls(array, 2, 3):
    #    print("Too many rolls")
    print("Accessible rolls:", accessibleroll)
    totalroll += accessibleroll
    for r in range(len(array)):
        for c in range(len(array[r])):
            if array[r][c] == 'x':
                array[r][c] = '.'
print("Total rolls:", totalroll)
