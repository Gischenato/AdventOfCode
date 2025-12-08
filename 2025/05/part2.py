ranges = []
ids = []
add_ids = False
for line in open('in'):
    if line.strip() == '':
        add_ids = True
        continue
    
    if not add_ids:
        ranges.append(list(map(int,line.strip().split('-'))))
    else:
        ids.append(int(line.strip()))

ranges.sort(key=lambda x: x[0])

new_ranges = [ranges.pop(0)]

while len(ranges) > 0:
    current_range = ranges.pop(0)
    print(f'Current range: {current_range}, new_ranges= {new_ranges}')
    if current_range[0] <= new_ranges[-1][1]:
        new_ranges[-1][1] = max(new_ranges[-1][1], current_range[1])

    else:
        new_ranges.append(current_range)

tot = 0
for r in new_ranges:
    tot += len(range(r[0], r[1]+1))
print(tot)