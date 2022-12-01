biggest = 0
acc = 0
for line in open('in'):
    if line.strip() == '':
        biggest = max(acc, biggest)
        acc = 0
        continue
    acc += int(line)
print(biggest)