mapa = []

for line in open('in'):
    mapa.append(line.strip())

start = (0, 0)
x, y = start

print(mapa)
print(mapa[x][y])

total = 0

while True:
    x, y = start
    x = (x + 3) % len(mapa[0])
    y = y + 1
    if y >= len(mapa):
        break
    print((x, y), (len(mapa), len(mapa[0])))
    if mapa[y][x] == '#':
        total += 1
    start = (x, y)

print(total)