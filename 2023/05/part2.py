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


ranges = list()
for i in range(0, len(seeds), 2):
    start, rng = seeds[i], seeds[i+1]
    ranges.append((int(start), int(start) + int(rng)))
print(ranges)



finals = [] 


def create_ranges(r1, r2):
    minimo, maximo = map(int, r1)
    start_r2, end_r2 = map(int, r2)
    if minimo > end_r2:
        # print(-1)
        return [r1]
    if maximo < start_r2:
        # print(0)
        return [r1]
    if minimo >= start_r2 and maximo <= end_r2:
        # print(1)
        return [r1]
    if minimo >= start_r2 and maximo >= end_r2:
        # print(2)
        return [(minimo, end_r2), (end_r2+1, maximo)]
    if minimo <= start_r2 and maximo <= end_r2:
        # print(3)
        return [(minimo, start_r2-1), (start_r2, maximo)]
    if minimo <= start_r2 and maximo >= end_r2:
        # print(4)
        return [(minimo, start_r2-1), (start_r2, end_r2), (end_r2+1, maximo)]
    print('ERROR create_ranges')    


def collapse_ranges(ranges):
    ranges = sorted(ranges, key=lambda x: x[0])  # Sort the ranges based on the start value
    merged_ranges = []
    for current_range in ranges:
        if not merged_ranges or merged_ranges[-1][1] < current_range[0]:
            merged_ranges.append(current_range)
        else:
            merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], current_range[1]))
    return merged_ranges



print('Almanac:')
ranges = set(ranges)
print(ranges)
c = 0
for a in almanac:
    print()
    print(f"====== ALMANAC {c} ======")
    # print(f'Ranges: {ranges}')
    c = c+1
    ok_ranges = set()
    for line in a:
        dst, src, rng = line
        full_rng = (int(src), int(src) + int(rng))
        diff = int(src) - int(dst)
        # print(dst, src, rng)
        print('full_rng', full_rng)
        print(f'To test: {ranges}')
        # print(f'line: {line}')
        # print(ranges)
        to_remove = set()
        for r in ranges:
            print(f'testing {r} in {full_rng}')
            s = create_ranges(r, full_rng)
            print('RESULT: ', s)
            for v in s:
                ini, fim = v
                if ini >= full_rng[0] and fim <= full_rng[1]:
                    print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
                    print(f'Encontrou {v} in {full_rng}')
                    print(f'({ini} -> {ini - diff}) ({fim} -> {fim - diff})')
                    print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
                    # print(f'AQUI {v} in {full_rng}')
                    new_v = (ini - diff, fim - diff)
                    # print(f'({ini} -> {new_v[0]}) ({fim} -> {new_v[1]})')
                    ok_ranges.add(new_v)
                    to_remove.add(v)
                # else:
                #     ranges.add(v)
            # print(f'Ranges: {ranges}')
            # print(f'-0-0-0-0-')
        # print(f'Ranges: {ranges}')
        ranges.difference_update(to_remove)
    # print('==============')
    # print(ranges)
    # print(ok_ranges)
    # print('---------------------------------------------------')
    # break
    ranges = ranges.union(ok_ranges)
    ranges = set(collapse_ranges(ranges))



sorted_ranges = sorted(ranges, key=lambda x: x[0])
for r in sorted_ranges:
    print(r)


minimo = 0
start = True
for r in ranges:
    if start:
        start = False
        minimo = r[0]
    else:
        if r[0] < minimo and r[0] != 0:
            minimo = r[0]
    
print(minimo)

# print(ranges)
# for r in ranges:
#     new_ranges = set()
#     new_ranges.add(r)
#     print('============')
#     print(r)
#     print(new_ranges)
#     print('============')
#     curr = 0
#     for a in almanac:
#         print(r, a)
#         for line in a:
#             dst, src, rng = line
#             full_rng = (int(src), int(src) + int(rng))
#             print(dst, src, rng, r, full_rng)
#             for s in create_ranges(r, full_rng):
#                 print('new range', s)
#                 new_ranges.add(s)
#             print('--------------------')

#         pass
#         print()
#     print(new_ranges)
#     break

# for seed in seeds:
#     curr = 0
#     for a in almanac:
#         find = False
#         curr += 1
#         for line in a:
#             dst, src, rng = line
#             if int(seed) >= int(src) and int(seed) <= int(src) + int(rng):
#                 diff = int(seed) - int(src)
#                 prox = int(dst) + diff
#                 seed = prox
#                 find = True
#                 break
#     finals.append(int(seed))





# print(min(finals))