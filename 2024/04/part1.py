data = []
for line in open('in'):
    data.append(list(line.strip()))
    
for l in data:
    print(l)

EMPTY = '' 
X    = 'X'
XM   = 'XM'
XMA  = 'XMA'
XMAS = 'XMAS'

search = {
    'X': 'M',
    'M': 'A',
    'A': 'S'
}
lines = len(data)
columns = len(data[0])
    
def find_xmas(line, column, curr: str, path):
    global X, XM, XMA, XMAS, EMPTY, lines, columns
    total = 0

    if curr not in [X, XM, XMA, XMAS, EMPTY]:
        return 0
    # print(curr, path)

    if curr == XMAS:
        print("FIND ONE", path)
        return 1

    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue

            nl = line + y
            nc = column + x

            if 0 <= nl < lines and 0 <= nc < columns:
                
                nxt = curr + data[nl][nc]
                total += find_xmas(
                    nl,
                    nc,
                    nxt,
                    path + [(nc, nl)]
                )

    return total

directions = {
    (0, 1): 'S',
    (1, 1): 'SE',
    (1, 0): 'E',
    (1, -1): 'NE',
    (0, -1): 'N',
    (-1, -1): 'NW',
    (-1, 0): 'W',
    (-1, 1): 'SW'
}

def explore():
    tot = 0
    for l in range(lines):
        for c in range(columns):
            if data[l][c] != 'X': continue
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if x == 0 and y == 0: continue
                    curr = 'X'
                    nl = l + y
                    nc = c + x
                    path = [(l,c)]
                    while curr in [X, XM, XMA, XMAS, EMPTY]:
                        print(curr, path, directions[(x,y)])
                        if 0 <= nl < lines and 0 <= nc < columns:
                            curr += data[nl][nc]
                            if curr == 'XMAS':
                                tot +=1
                                break
                        else:
                            break
                        path.append((nl,nc))
                        nl += y
                        nc += x

            # tot += find_xmas(l,c, 'X', [(c,l)])
            print(f'HERE {c} {l}')
        # print()
    print(tot)
        
explore()

