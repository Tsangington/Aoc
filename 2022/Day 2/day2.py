def part1():
    f = open("2022\Day 2\input.txt","r")
    points=0
    for line in f:
        line = line.removesuffix("\n")
        line = line.split(" ")
        line[1]= chr(ord(line[1])-23)
        if line[0] == line[1]: #draw
            points+= 3 + int(ord(line[1])-64)
        elif int(ord(line[1])) - int(ord(line[0])) == 1 or line[1] == "A" and line[0] == "C": #win
            points+= (6 + int(ord(line[1])-64))
        else: #lose
            points+=int(ord(line[1])-64)
    print(points)

def part2():
    f = open("2022\Day 2\input.txt","r")
    points=0
    win = {
        "A":"B",
        "B":"C",
        "C":"A"
        }
    lose = {
        "B":"A",
        "C":"B",
        "A":"C"
    }
    for line in f:
        line = line.removesuffix("\n")
        line = line.split(" ")
        if line[1] == "Y" :#draw
            points+= 3 + int(ord(line[0])-64)
        elif line[1] == "Z": #win
            points+= (6 + int(ord(win[line[0]]))-64)
        else: #lose
            points+=int(ord(lose[line[0]]))-64
    print(points)
part2()