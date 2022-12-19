valves = dict()
tunnels = dict()

for line in open('in'):
    valve = line.split()[1]
    flowRate = int(line.split()[4].split('=')[1].replace(';', ''))
    targets = line.split('to')[1].replace(',', '').split()[1:]
    valves[valve] = flowRate
    tunnels[valve] = targets

distances = dict()
none_empty = []

for valve in valves:
    if valve != 'AA' and not valves[valve]: continue
    if valve != 'AA': none_empty.append(valve)

    distances[valve] = {valve:0, 'AA': 0}
    visited = set(valve)

    queue = [(0, valve)]

    while queue:
        distance, position = queue.pop(0)
        for neightbor in tunnels[position]:
            if neightbor in visited: continue
            visited.add(neightbor)

            if valves[neightbor]: distances[valve][neightbor] = distance+1
            queue.append((distance+1, neightbor))

    del distances[valve][valve]
    if valve != 'AA':
        del distances[valve]['AA']
    
CACHE = dict()

indicies = dict()
for index, element in enumerate(none_empty):
    indicies[element] = index

'''
BITMASK:
the indicies can be represented in binary
then, we can shift the bit << 1 to the left
this will create a mask representing the position of the valve
indicies: 
GV 0  -> 0000 => 000000000000001 
NK 1  -> 0001 => 000000000000010 
IG 2  -> 0010 => 000000000000100 
VZ 3  -> 0011 => 000000000001000 
LJ 4  -> 0100 => 000000000010000 
TO 5  -> 0101 => 000000000100000 
RF 6  -> 0110 => 000000001000000 
YV 7  -> 0111 => 000000010000000 
TX 8  -> 1000 => 000000100000000 
YF 9  -> 1001 => 000001000000000 
QK 10 -> 1010 => 000010000000000 
VP 11 -> 1011 => 000100000000000 
HP 12 -> 1100 => 001000000000000 
QL 13 -> 1101 => 010000000000000 
VB 14 -> 1110 => 100000000000000
'''

def depth_search(time, valve, bitmask):
    global distances
    if (time, valve, bitmask) in CACHE: return CACHE[(time, valve, bitmask)]
    maxval = 0
    for neighborn in distances[valve]:
        bit = 1 << indicies[neighborn]
        if bitmask & bit: continue
        remaining_time = time - distances[valve][neighborn] - 1
        if remaining_time <= 0: continue
        maxval = max(maxval ,depth_search(remaining_time, neighborn, bitmask | bit) + valves[neighborn] * remaining_time)
    CACHE[(time, valve, bitmask)] = maxval
    return maxval

b = (1 << len(none_empty)) - 1
 

maximun = 0
for i in range((b + 1) // 2):
    maximun = max(maximun, depth_search(26, "AA", i) + depth_search(26, "AA", b ^ i))

print(maximun)
# print(depth_search(30, "AA", 0))