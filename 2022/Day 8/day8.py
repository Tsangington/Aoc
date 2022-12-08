def part1():
    listCoords = []
    for y in range(len(grid[0])): #left --> right
        low = -1
        for x in range(len(grid)):
            if int(grid[y][x]) > low:
                listCoords.append([y,x])
                low = int(grid[y][x])
    
    for y in range(len(grid[0]) -1, -1, -1): #right --> left
        low = -1
        for x in range(len(grid) -1, -1 ,-1):
            if int(grid[y][x]) > low:
                listCoords.append([y,x])
                low = int(grid[y][x])
    
    for x in range(len(grid)): #top --> bottom
        low = -1
        for y in range(len(grid[0])):
            if int(grid[y][x]) > low:
                listCoords.append([y,x])
                low = int(grid[y][x])
    
    for x in range(len(grid) -1, -1, -1): #bottom --> top
        low = -1
        for y in range(len(grid[0]) -1, -1, -1):
            if int(grid[y][x]) > low:
                listCoords.append([y,x])
                low = int(grid[y][x])

    listCoords.sort()
    visible = []
    for coords in listCoords:
        if coords not in visible:
            visible.append(coords)
    print(len(visible))

def part2():
    score = []
    for y in range(len(grid[0])): 
        for x in range(len(grid)):
            score.append(searchFrom(x, y))
    
    score.sort(reverse= True)
    print(score[0])

def searchFrom(startX ,startY):
    leftScore = 0
    rightScore = 0
    topScore = 0
    downScore = 0
    max  = grid[startY][startX]

    for x1 in range(startX + 1, len(grid)): #Right of the tree
        if grid[startY][x1] < max:
            rightScore += 1
        else:
            rightScore +=1
            break

    for x2 in range(startX -1, -1,-1): #Left of the tree
        if grid[startY][x2] < max:
            leftScore +=1
        else:
            leftScore +=1
            break

    for y1 in range(startY -1, -1, -1): #Above the tree
        if grid[y1][startX] < max:
            topScore +=1
        else:
            topScore +=1
            break

    for y2 in range(startY + 1 ,len(grid[0])): #Below of the tree
        if grid[y2][startX] < max:
            downScore +=1
        else:
            downScore +=1
            break
    totalScore = leftScore * rightScore * topScore * downScore
    return(totalScore)

grid = []
f = open("2022\Day 8\input.txt","r")
for line in f:
    line = line.removesuffix("\n")
    grid.append(list(line))
[[int(x) for x in row] for row in grid]

part1()
part2()