inp = [line.strip() for line in open('in')]
trees = []
for treeRow in inp:
    row = []
    for tree in treeRow:
        row.append(tree)
    trees.append(row)

def isValid(row, col):
    global trees
    return (row >= 0 and row < len(trees)) and (col >= 0 and col < len(trees[0]))

def explore(row, col, tree):
    global trees
    if not isValid(row, col): return 2
    return 1 if trees[row][col] < tree else 0

find = []
for i in range(len(trees)):
    for j in range(len(trees[i])):
        tree = trees[i][j]
        ok = True
        # left
        left = True
        for col in range(0, j):
            left = left and explore(i, col, tree)
        if left: 
            find.append((i,j))
            continue
        # right
        right = True
        for col in range(j+1, len(trees[i])):
            right = right and explore(i, col, tree)
        if right:
            find.append((i,j))
            continue
        # top
        top = True
        for line in range(0, i):
            top = top and explore(line, j, tree)
        if top:
            find.append((i,j))
            continue
        # bottom
        bottom = True
        for line in range(i+1, len(trees)):
            bottom = bottom and explore(line, j, tree)
        if bottom:
            find.append((i,j))
            continue


def scenic_score(row, col):
    global trees
    values = {'top':0, 'bottom':0, 'left':0, 'rigth':0}
    tree = trees[row][col]
    for i in range(row-1, -1, -1):
        values['left'] += 1
        if trees[i][col] >= tree: break
    # right
    for i in range(row+1, len(trees)):
        values['rigth'] += 1
        if trees[i][col] >= tree: break
    # top
    for j in range(col-1, -1, -1):
        values['top'] += 1
        if trees[row][j] >= tree: break
    # bottom
    for j in range(col+1, len(trees[row])):
        values['bottom'] += 1
        if trees[row][j] >= tree: break

    # print(f'({row},{col} -> {values}')
    return values['bottom'] * values['left'] * values['top'] * values['rigth'] 

max_score = 0
for tree in find:
    i, j = tree
    score = scenic_score(i,j)
    max_score = max(max_score, score)
print(max_score)