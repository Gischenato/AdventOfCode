mapa = []

for line in open('in'):
    mapa.append(line.strip())


def run(incX, incY):
    total = 0
    start = (0, 0)
    while True:
        x, y = start
        x = (x + incX) % len(mapa[0])
        y = y + incY
        if y >= len(mapa):
            print("AQUI")
            break
        print((x, y), (len(mapa), len(mapa[0])))
        if mapa[y][x] == '#':
            total += 1
        start = (x, y)
    return total

v1, v2, v3, v4, v5 = run(1,1), run(3,1), run(5,1), run(7,1), run(1,2)
print(v1, v2, v3, v4, v5)
print(v1 * v2 * v3 * v4 * v5)