data = []

for line in open('in'):
    data.append(line.strip())



total = 0

def isValid(x,y):
    return x >= 0 and x < len(data[0]) and y >= 0 and y < len(data)

def check(line, col):
    tot = 0
    for y in [0,1,-1]:
        for x in [0,1,-1]:
            if x == 0 and y == 0: continue
            if isValid(col+x,line+y):
                print(f'Accessing {[line+y]},{[col+x]}')
                if data[line+y][col+x] == '@': tot+=1
    
    return tot < 4

for line in range(len(data)):
    for col in range(len(data[0])):
        if data[line][col] != '@': continue
        if check(line, col):
            total += 1

print(total)
