mapa = [[char for char in line.strip()] for line in open('in')]
arestas = []

for i in range(len(mapa)):
    toAdd = []
    for j in range(len(mapa[i])):
        toAdd.append([1e8, '_'])
    arestas.append(toAdd)


start = ()
end = ()
for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        if mapa[i][j] == 'S':
            start = (i, j)
            mapa[i][j] = 'a'
        elif mapa[i][j] == 'E':
            end = (i,j)
            mapa[i][j] = 'z'

def isValid(i, j):
    global mapa
    return i >= 0 and i < len(mapa) and j >= 0 and j < len(mapa[i])

def explore(i, j, came_from, visited):
    global mapa, arestas, end
    if not isValid(i, j): return 
    if (i,j) in visited: return

    from_letter = mapa[came_from[0]][came_from[1]]
    from_value = arestas[came_from[0]][came_from[1]][0]
    current_letter = mapa[i][j]
    current_value = from_value+1
    if current_value >= arestas[i][j][0]:return
    if ord(current_letter) - ord(from_letter) > 1: return
    if (i, j) == end:
        arestas[i][j] = [current_value, from_letter, came_from]
        return 
    arestas[i][j] = [current_value, from_letter, came_from]

    visited.add((i, j))

    for pos in [(0,1), (0,-1), (1, 0), (-1, 0)]:
        row, col = pos
        explore(i+row, j+col, (i, j), visited.copy())

def dijkstra(start):
    global arestas
    i, j = start
    arestas[i][j] = [0, '_']
    for pos in [(0,1), (0,-1), (1, 0), (-1, 0)]:
        row, col = pos
        explore(i+row, j+col, (i, j), set())

for i in mapa:
    for l in i:
        print(l, end='')
    print()

dijkstra(start)
print(arestas[end[0]][end[1]])