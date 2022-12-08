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
    if not isValid(row, col): return True
    return trees[row][col] < tree

total = 0
for i in range(len(trees)):
    for j in range(len(trees[i])):
        tree = trees[i][j]
        ok = True
        # left
        left = True
        for col in range(0, j):
            left = left and explore(i, col, tree)
        if left: 
            total+=1
            continue
        # right
        right = True
        for col in range(j+1, len(trees[i])):
            right = right and explore(i, col, tree)
        if right:
            total+=1
            continue
        # top
        top = True
        for line in range(0, i):
            top = top and explore(line, j, tree)
        if top:
            total+=1
            continue
        # bottom
        bottom = True
        for line in range(i+1, len(trees)):
            bottom = bottom and explore(line, j, tree)
        if bottom:
            total+=1
            continue

print(total)