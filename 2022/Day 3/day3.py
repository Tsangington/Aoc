import numpy as np

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def part1():
    f = open("2022\Day 3\input.txt","r")
    piorities=0
    for line in f:
        ignore = []
        line = line.replace("\n","")
        line= list(line)
        bp1,bp2 = split_list(line)
        for item in bp2:
            if item in bp1 and item not in ignore:
                if item.islower() == True:
                    piorities+=(ord(item)-96)
                else:
                    piorities+=(ord(item)-38)
                ignore.append(item)
    print(piorities)

def part2():
    f = open("2022\Day 3\input.txt","r")
    piorities=0
    elves=[]

    for line in f:
        line = line.strip("\n")
        elves.append(line)
    elves = np.array_split(elves,len(elves)/3)
    for group in elves:
        item = ''.join(set(group[0]).intersection(set(group[1]),set(group[2])))
        if item.islower() == True:
            piorities+=(ord(item)-96)
        else:
            piorities+=(ord(item)-38)  
    print(piorities)      
part2()