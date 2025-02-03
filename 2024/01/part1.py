l1,l2 = [],[]

for l in open('in'):
    v1,v2 = map(int, l.strip().split())
    l1.append(v1)
    l2.append(v2)
    
l1.sort()
l2.sort()

print(sum([abs(l1[i]-l2[i]) for i in range(len(l1))]))