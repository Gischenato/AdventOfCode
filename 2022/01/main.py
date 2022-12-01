biggest = []
acc = 0
for line in open('in'):
    if line.strip() == '':
        if len(biggest) == 3:
            biggest = sorted(biggest)
            biggest[0] = max(acc, biggest[0])
        else:
            biggest.append(acc)
        acc = 0
        continue
    acc += int(line)

print(sum(biggest))