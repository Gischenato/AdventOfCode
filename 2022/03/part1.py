count = 1
values = dict()
for i in range(ord('a'),ord('z')+1):
    values[chr(i)] = count
    count += 1
for i in range(ord('A'),ord('Z')+1):
    values[chr(i)] = count
    count += 1

total = 0
for line in open('in'):
    letters1 = set()
    letters2 = set()
    line = line.strip()
    j = len(line)-1
    for i in range(j):
        if i >= j: break
        letters1.add(line[i])
        letters2.add(line[j])
        j -= 1    
    for letter in letters1:
            total+=values[letter] if letter in letters2 else 0
print(total)
