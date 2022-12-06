
def moveCrates9000(query): #query[0] = num, query[1] is from, query[2] is to
    for _ in range(query[0]):
        temp = crate[query[1]-1].pop()
        crate[query[2]-1].append(temp)

def moveCrates9001(query):
    stack = crate[query[1]-1][-(query[0]):]
    for x in range(len(stack)):
        crate[query[2]-1].append(stack[x])
    for _ in range(query[0]):
        crate[query[1]-1].pop()

crate = [[],[],[],[],[],[],[],[],[]]

def solve(part):
    f = open("2022\Day 5\input.txt","r")
    array = []

    first = True
    answer = ""
    
    for line in f:
        if line[0]=="[" or line[0]== " ":
            for terms in (("[", " "), ("]", ""), ("    ", "0"), (" ","")):
                line = line.replace(*terms)
            line = line.strip("\n")
            array.append(list(line))

        if first == True and len(array) == 9:
            array.remove(array[8])
            for num in range(len(array)-1, -1, -1):
                for num2 in range(len(array[0])):
                    if array[num][num2] != "0":
                        crate[num2].append(array[num][num2])
            first = False
    
        if line[0] == "m":
            line = line.strip("\n")
            for terms in (("move ", ""), ("from ", ""), ("to ", "")):
                line = line.replace(*terms)
            query = line.split(" ")
            query = [int(x) for x in query]
            part(query)

    for y in crate:
        answer+=str(y[-1:])
    print(answer)

solve(moveCrates9000)
solve(moveCrates9001)

