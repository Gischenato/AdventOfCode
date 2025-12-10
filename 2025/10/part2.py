# Doesnt work for input, just for example

data = [x.split() for x in open('ex').read().strip().split('\n')]
tot = 0

for line in data:
    print(line)
    entry, switches, outcome = list(line[0][1:-1]), line[1:-1], line[-1][1:-1]
    switches = [list(map(int,(l[1:-1].split(',')))) for l in switches]
    outcome = tuple(int(x) for x in outcome.split(','))
    # print(outcome)
    start = [0 for _ in range(len(entry))]
    # print(start)


    SEEN = set()
    SEEN.add(tuple(start))
    to_visit = [(start, 0)]
    # print(SEEN)
    while True:
        curr, path = to_visit.pop(0)
        print(curr)
        find = False
        for s in switches:
            new_state = curr.copy()
            for i in s:
                new_state[i] += 1
            value = tuple(new_state)
            # print(value, path+1)
            if value == outcome:
                tot += path+1
                find = True
                break
            if value not in SEEN:
                SEEN.add(value)
                to_visit.append((new_state, path+1))
        if find:
            break

print(tot)
