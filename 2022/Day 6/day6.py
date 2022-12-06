def unique(code, length):
    if len( set( code)) == length:
        return(True)

def solve(line, type):
    for index in range(len(line)):
        if unique( line[ index: index+ type], type) == True:
                return("The marker appeared by index: {characterNum}".format(characterNum = index+type))

f = open("2022\Day 6\input.txt","r")
line = f.readline()
marker = 4
message = 14
print(solve(line, marker))
print(solve(line, message))