tot = 0

for line in open('in'):
    line = line.strip()
    j = len(line) - 1
    first = False
    value = ''
    curr = ''
    print(line)
    for i in range(len(line)):
        if line[i].isnumeric():
            if not first:
                first = True
                value += line[i]
            curr = line[i]
    value += curr
    
    print(value)
    tot += int(value)

print(tot)