mapa = []

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
            # print(value)``
            if not value == '.' and not value.isnumeric():
                return True
        if y - 1 >= 0:
            value = mapa[y - 1][x]
            # print(value)
            if not value == '.' and not value.isnumeric():
                return True
    if min_x - 1 >= 0:
        for y_acc in (-1, 0, 1):
            if y + y_acc >= 0 and y + y_acc < len(mapa):
                value = mapa[y + y_acc][min_x - 1]
                # print(value)
                if not value == '.' and not value.isnumeric():
                    return True
    if max_x + 1 < len(mapa[0]):
        for y_acc in (-1, 0, 1):
            if y + y_acc >= 0 and y + y_acc < len(mapa):
                value = mapa[y + y_acc][max_x + 1]
                # print(value)
                if not value == '.' and not value.isnumeric():
                    return True
                
    return False


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
                if check(xs, y):
                    tot += int(curr)
                    add.append((curr, xs, y))
                else:
                    n_add.append((curr, xs, y))
            curr = ''
            xs = []
    if len(curr) > 0:
        if check(xs, y):
            tot += int(curr)
            add.append((curr, xs, y))
        else:
            n_add.append((curr, xs, y))
    y += 1

print(tot)
