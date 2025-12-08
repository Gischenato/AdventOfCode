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

print(new_ranges)

def is_in_ranges(id, ranges):
    if len(ranges) == 0: return False
    curr = len(ranges)//2
    print(ranges[curr], id)
    curr_range = ranges[curr]
    if id in range(curr_range[0], curr_range[1]+1):
        print("HERE")
        return True
    elif id < curr_range[0]:
        return is_in_ranges(id, ranges[:curr])
    elif id > curr_range[1]:
        return is_in_ranges(id, ranges[curr+1:])


tot = []
for id in ids: 
    if is_in_ranges(id, new_ranges): tot.append(id)
    
print(len(tot))
