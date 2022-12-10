cycle = 0
x = 1
led = ['.' for _ in range(40)]

def draw():
    global cycle, x, led
    if cycle-1 == x or cycle-1 == x-1 or cycle-1 == x+1:
        led[cycle-1] = '#'
    if cycle%40 == 0:
        cycle = 0
        for pixel in led: print(pixel, end='')
        print()
        led = ['.' for _ in range(40)]
    
for line in open('in'):
    line = line.strip().split()
    if line[0] == 'addx':
        cycle+=1
        draw()
        cycle+=1
        draw()
        x += int(line[1])
    elif line[0] == 'noop':
        cycle+=1
        draw()