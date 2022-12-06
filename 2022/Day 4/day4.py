def intersection(elf1,elf2): 
    if elf1[0]==elf2[0] or elf1[1]==elf2[1]:
        return(1)
    if elf1[0]<elf2[0] and elf1[1]>elf2[1]:
        return(1)
    if elf2[0]<elf1[0] and elf2[1]>elf1[1]:
        return(1)
    return(0)

def intersectionP2(elf1,elf2):
    if elf1[0]<=elf2[1] and elf2[0]<=elf1[1]:
        return(1)
    if elf2[0]<=elf1[1] and elf1[0]<=elf2[1]:
        return(1)
    return(0)

f = open("2022\Day 4\input.txt","r")
count=0
count2=0
for line in f:
    elf=[]
    line = line.removesuffix("\n")
    line = line.split(",")
    elf.append(line[0].split("-"))
    elf.append(line[1].split("-"))
    elf[0][0] = int(elf[0][0])
    elf[0][1] = int(elf[0][1])
    elf[1][0] = int(elf[1][0])
    elf[1][1] = int(elf[1][1])  
    count += intersection(elf[0],elf[1])
    count2 += intersectionP2(elf[0],elf[1])
    print(elf[0], elf[1], intersectionP2(elf[0] ,elf[1]))
print(count, count2)