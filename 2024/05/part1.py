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
        
print(maping)

tot = 0
for u in updates:
    update_order = u.split(',')
    for v in update_order[:-1]:
        next = update_order[update_order.index(v)+1]
        
        if next not in maping[v]:
            # print('NOT OK:', u)
            break
    else:
        print('OK:', u)
        tot += int(update_order[len(update_order)//2]) 
print(tot) 