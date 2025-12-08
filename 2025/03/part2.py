tot = 0
for line in open('in'):
    line = list(line.strip())
    curr = 1

    while True:
        if len(line) == 12 or curr >= len(line): break
        if int(line[curr]) > int(line[curr-1]):
            line.pop(curr-1)
            curr -= 1
        else: curr += 1
        if curr == 0: curr = 1
    tot += int(''.join(line[:12]))

print(tot)