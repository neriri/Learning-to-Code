import random, time, copy
Width = 6
Height = 6

nextCell = []
for x in range(Width):
    column = []
    for y in range(Height):
        if random.randint(0,1) == 0:
            column.append('#')
        else:
            column.append(' ')
    nextCell.append(column)
while True:
    print('\n\n\n\n\n')
    currentCell = copy.deepcopy(nextCell)

    for y in range(Height):
        for x in range(Width):
            print(currentCell[x][y], end='')
        print()

    for x in range(Width):
        for y in range(Height):
            leftCoord =(x-1)% Width
            rightCoord =(x+1)% Width
            aboveCoord = (y-1)% Height
            belowCoord = (y+1)% Height

            numNeighbors = 0
            if currentCell[leftCoord][aboveCoord] == '#':
                numNeighbors +=1
            if currentCell[x][aboveCoord] == '#':
                numNeighbors += 1
            if currentCell[rightCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCell[leftCoord][y] == '#':
                numNeighbors += 1
            if currentCell[rightCoord][y] == '#':
                numNeighbors += 1
            if currentCell[leftCoord][belowCoord] == '#':
                numNeighbors += 1
            if currentCell[x][belowCoord] == '#':
                numNeighbors += 1
            if currentCell[rightCoord][belowCoord] == '#':
                numNeighbors += 1


            if currentCell[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                nextCell[x][y] = '#'
            elif currentCell[x][y] == ' ' and numNeighbors == 3:
                nextCell[x][y] = '#'
            else:
                nextCell[x][y] = ' '
    time.sleep(1)
