f = open("2022\Day 1\input.txt","r")
total=0
calories = []
for line in f:
    if line=='\n':
        calories.append(total)
        total=0
    else:
        total+=int(line)

calories.sort()
print(calories[-1])
print(sum(calories[-3:]))