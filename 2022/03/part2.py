count = 1
values = dict()
for i in range(ord('a'),ord('z')+1):
    values[chr(i)] = count
    count += 1
for i in range(ord('A'),ord('Z')+1):
    values[chr(i)] = count
    count += 1

total = 0
count = 1
groups = dict()
for i in range(1, 4): groups[i] = set()
for line in open('in'):
    for letter in line.strip():
        groups[count].add(letter)
    count += 1
    if count > 3:
        total += values[list(groups[1] & groups[2] & groups[3])[0]]
        for key in groups.keys(): groups[key] = set()
        count = 1
print(total)