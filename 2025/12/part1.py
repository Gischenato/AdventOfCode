data = open('in').read().split('\n\n')

blocks = data[0:-1]
lines = data[-1].split('\n')


for i, block in enumerate(blocks):
    block = block.split('\n')[1:]
    blocks[i] = block

total = 0

for i, line in enumerate(lines):
    size, to_use = line.split(':')
    size = list(map(int, size.split('x')))
    to_use = list(map(int, to_use.strip().split()))
    print(size, to_use)
    
    tot = size[0]*size[1]
    acc = 0
    for i, b in enumerate(to_use):
        if b > 0:
            block = blocks[i]
            acc_2 = 0
            for l in block:
                acc_2 += l.count('#')
            acc += acc_2*b
    print(acc, tot)
    if acc < tot:
        total+=1
    
print(total)
