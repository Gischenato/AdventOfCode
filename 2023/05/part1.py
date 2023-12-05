seeds_to_find = True
seeds = []

almanac = []

mapa = []
for line in open('in'):
    if seeds_to_find:
        seeds_to_find = False
        _, seed = line.strip().split(':')
        seeds = seed.strip().split(' ')
        continue

    line = line.strip()

    if line == '':
        mapa = [] 
        almanac.append(mapa)
        continue
    
    if line.endswith(':'):
        continue

    mapa.append(line.split(' '))

finals = [] 

for seed in seeds:
    curr = 0
    for a in almanac:
        find = False
        curr += 1
        for line in a:
            dst, src, rng = line
            if int(seed) >= int(src) and int(seed) <= int(src) + int(rng):
                diff = int(seed) - int(src)
                prox = int(dst) + diff
                seed = prox
                find = True
                break
    finals.append(int(seed))

print(min(finals))