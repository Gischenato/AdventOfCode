data = [x.split() for x in open('in').read().strip().split('\n')]

reverse = {
    '.': '#',
    '#': '.'
}

for line in data:
    entry, switches = list(line[0][1:-1]), line[1:-1]
    switches = [list(map(int,(l[1:-1].split(',')))) for l in switches]
    print(entry)
    SEEN = set()
    SEEN.add(''.join(entry))
    to_visit = [(entry, [])]
    print(SEEN)

    while True:
        curr, path = to_visit.pop(0)
        find = False
        for s in switches:
            new_state = curr.copy()
            for i in s:
                new_state[i] = reverse[new_state[i]]
            value = ''.join(new_state)
            ok = set(value)
            new_path = path + [s]
            print(value, new_path)
            if len(ok) == 1 and '.' in ok:
                print(len(new_path))
                print(new_path)
                print('--------')
                tot += len(new_path)
                find = True
                break
            if value not in SEEN:
                SEEN.add(value)
                to_visit.append((new_state, new_path))
        if find:
            break

print(tot)
