count = 1
values = dict()
for i in range(ord('a'),ord('z')+1):
    values[chr(i)] = count
    count += 1
for i in range(ord('A'),ord('Z')+1):
    values[chr(i)] = count
    count += 1

total = 0
groups = []
count = 1
groups = {
    1: set(),
    2: set(),
    3: set()
}
for line in open('in'):
    for letter in line.strip():
        groups[count].add(letter)
    count += 1
    if count > 3:
        for l1 in groups[1]:
            if l1 in groups[2] and l1 in groups[3]:
                total += values[l1]
        groups = {
            1: set(),
            2: set(),
            3: set()
        }
        count = 1

print(total)
