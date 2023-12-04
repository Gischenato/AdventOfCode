mapa = []
gears = {}


def check(xs: list, y):
    global mapa
    min_x = min(xs)
    max_x = max(xs)

    # for x in xs:
    #     print(mapa[y][x], end='')

    # print()

    for x in xs:
        if y + 1 < len(mapa):
            value = mapa[y + 1][x]
            # print(value)
            if value == '*':
                return True, (x, y+1)
        if y - 1 >= 0:
            value = mapa[y - 1][x]
            # print(value)
            if value == '*':
                return True, (x, y-1)
    if min_x - 1 >= 0:
        for y_acc in (-1, 0, 1):
            if y + y_acc >= 0 and y + y_acc < len(mapa):
                value = mapa[y + y_acc][min_x - 1]
                # print(value)
                if value == '*':
                    return True, (min_x-1, y+y_acc)
    if max_x + 1 < len(mapa[0]):
        for y_acc in (-1, 0, 1):
            if y + y_acc >= 0 and y + y_acc < len(mapa):
                value = mapa[y + y_acc][max_x + 1]
                # print(value)
                if value == '*':
                    return True, (max_x+1, y+y_acc)
                
    return False, None


for line in open('in'):
    mapa.append(line.strip())


add = []
n_add = []
tot = 0

curr = ''
xs = [] 

y = 0
for line in mapa:
    curr = ''
    xs = [] 
    for i in range(0, len(line)):
        value = line[i]
        if value.isnumeric():
            curr += value
            xs.append(i)
        else:
            if len(curr) > 0:
                ok, pos = check(xs, y)
                if ok:
                    X, Y = pos
                    gear = gears.get((X, Y), [])
                    gear.append(curr)
                    gears[(X, Y)] = gear
            curr = ''
            xs = []
    if len(curr) > 0:
        ok, pos = check(xs, y)
        if ok:
            X, Y = pos
            gear = gears.get((X, Y), [])
            gear.append(curr)
            gears[(X, Y)] = gear
    y += 1

t = 0
for k in gears:
    # print(k, gears[k])
    if len (gears[k]) == 2:
        t += int(gears[k][0]) * int(gears[k][1])

print(t)
# print(check([2,3,4], 6))