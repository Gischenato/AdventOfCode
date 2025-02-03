unsafe = 0 
tot = 0
for l in open('in'):
    tot += 1
    l = list(map(int, l.split()))
    if not(l == sorted(l) or l == sorted(l, reverse=True)):
        unsafe += 1
        continue
    l.sort()
    
    curr = l[0]
    for i in range(1, len(l)):
        dist = l[i] - curr
        if dist > 3 or dist <= 0:
            unsafe += 1
            print(tot, l)
            break
        curr = l[i]

print(tot - unsafe)