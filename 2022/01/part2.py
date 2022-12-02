biggest = []
acc = 0
for line in open('in'):
    if line.strip() == '':
        biggest.append(acc)
        acc = 0
        continue
    acc += int(line)
print(sum((sorted(biggest, reverse=True)[:3])))