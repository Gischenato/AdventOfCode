total = 0
for line in open('in'):
    set1 = set()
    set2 = set()
    elf1, elf2 = [[int(v1), int(v2)] for v1,v2 in (x.split('-') for x in line.strip().split(','))]
    set1.update(i for i in range(elf1[0], elf1[1]+1))
    set2.update(i for i in range(elf2[0], elf2[1]+1))
    if len(set1 & set2) != 0 or len(set1 & set2) != 0:
        total+=1
print(total)