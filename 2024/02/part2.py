def ok(xs):
    if not(xs==sorted(xs) or xs==sorted(xs,reverse=True)): return False
    ok = True
    for i in range(len(xs)-1):
        diff = abs(xs[i]-xs[i+1])
        if not 1<=diff<=3:
            return False
    return True

tot = 0
for l in open('in'):
    l = list(map(int, l.split()))
    good = False
    for j in range(len(l)):
        xs = l[:j] + l[j+1:]
        if ok(xs):
            good = True
            break
    if good: tot +=1
    
print(tot)