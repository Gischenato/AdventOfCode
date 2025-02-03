l1,l2 = [],[]

for l in open('in'):
    v1,v2 = map(int, l.strip().split())
    l1.append(v1)
    l2.append(v2)
    

calcs = {}


tot = 0
for i in l1:
    if i in calcs:
        tot += calcs[i]
        continue
    c = i*l2.count(i)
    tot += c
    calcs[i] = c
    
print(tot)