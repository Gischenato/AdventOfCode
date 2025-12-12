devices = {}

for line in open('ex2'):
    key, d = line.split(':')
    d = d.strip().split()
    devices[key] = set(d)

to_visit = [('svr', [])]
tot = 0
while True:
    if len(to_visit) == 0: break
    curr, path = to_visit.pop(0)
    if curr == 'out':
        tot += 1
        print(path + [curr])
        continue
    for d in devices[curr]:
        to_visit.append((d, path+[curr]))

print(tot)
