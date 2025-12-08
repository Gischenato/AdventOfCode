data = []
total = 0

for line in open('in'):
    data.append(list(line.strip()))

def isValid(x,y):
    return x >= 0 and x < len(data[0]) and y >= 0 and y < len(data)

def check(line, col):
    tot = 0
    for y in [0,1,-1]:
        for x in [0,1,-1]:
            if x == 0 and y == 0: continue
            if isValid(col+x,line+y):
                if data[line+y][col+x] == '@': tot+=1
    
    return tot < 4

while True:
    removed = False
    for line in range(len(data)):
        for col in range(len(data[0])):
            if data[line][col] != '@': continue
            if check(line, col):
                data[line][col] = '.'
                total += 1
                removed = True
    if not removed:
        break


print(total)
