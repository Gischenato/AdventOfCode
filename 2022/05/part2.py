piles = [[],[],[],[],[],[],[],[],[]]

def main():
    global piles
    inp = loadPiles()
    execute(inp)
    printPiles()
    for pile in piles:
        if pile: print(pile[-1], end='')

def loadPiles():
    global piles
    inp = [line for line in open('in')]
    toRemove = []
    for val in inp:
        toRemove.append(val)
        if val.startswith(' 1'): 
            break
        count = 0
        pile = 0
        for char in val:
            if count == 1 and not char == ' ':
                print('adding ' + char + ' to pile ' + str(pile+1))
                piles[pile].append(char) 
            count+=1
            if count == 4:
                count = 0
                pile += 1
    for val in toRemove:
        inp.remove(val)
    for pile in piles:
        pile = pile.reverse()
    return inp

def move(frm, to, qnt):
    global piles
    print('moving ' + str(qnt) + ' from pile ' + str(frm) + ' to pile ' + str(to))
    toAdd = []
    for _ in range(qnt):
        toAdd.append(piles[frm].pop())
    toAdd.reverse()
    for val in toAdd:
        piles[to].append(val)

def execute(inp):
    for val in inp:
        val = val.strip()
        if val == '': continue
        val = val.split(' ')
        qnt, frm, to = int(val[1]), int(val[3])-1, int(val[5])-1
        printPiles()
        move(frm, to, qnt)

def printPiles():
    global piles
    print('=======================')
    for pos,pile in enumerate(piles): 
        print(pos, ':', pile)
    print('=======================')

main()