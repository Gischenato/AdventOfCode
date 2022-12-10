cycle = 0
x = 1
total = 0

def calculateSignal():
    global cycle, x
    if cycle == 20 or (cycle - 20)%40 == 0:
        return cycle * x
    return 0
    
for line in open('in'):
    line = line.strip().split()
    if   line[0] == 'addx':
        cycle += 1
        total += calculateSignal()
        cycle += 1
        total += calculateSignal()
        x += int(line[1])
    elif line[0] == 'noop':
        cycle += 1
        total += calculateSignal()

print(total)