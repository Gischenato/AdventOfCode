order, updates = open('in').read().split('\n\n')

order = order.splitlines()
updates = updates.splitlines()

maping = {}

for o in order:
    before, after = o.split('|')
    print(before, '->', after)
    if before not in maping:
        maping[before] = {after}
    else:
        maping[before].add(after)
    if after not in maping:
        maping[after] = set()
        
for k in maping:
    print(k, '->', maping[k])

tot = 0
for u in updates:
    update_order = u.split(',')
    
    for v in update_order[:-1]:
        next = update_order[update_order.index(v)+1]
        
        if next not in maping[v]:
            break
    else:
        continue
    i = 0
    while i < len(update_order)-1:
        v = update_order[i]
        next = update_order[i+1]
        if next not in maping[v]:
            update_order[i], update_order[i+1] = update_order[i+1], update_order[i]
            i = 0
        else:
            i += 1
    print('FIXED:', ','.join(update_order))
    tot += int(update_order[len(update_order)//2])
    
print(tot) 