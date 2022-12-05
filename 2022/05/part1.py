piles = [[],[],[],[],[],[],[],[],[]]
t = 0

inp = [line.strip() for line in open('test')]

toRemove = []
for val in inp:
    toRemove.append(val)
    if val.startswith('1'): 
        break
    count = 0
    pile = 0
    for char in val:
        if count == 1 and not char == ' ':
            piles[pile].append(char) 
        count+=1
        if count == 4:
            count = 0
            pile += 1
for val in toRemove:
    inp.remove(val)

def move(frm, to, qnt):
    global piles
    for _ in range(qnt):
        piles[to].append(piles[frm].pop())
        # val = pile[frm].pop()

def printPiles():
    global piles
    print('=======================')
    for p in piles: 
        print(p)
    print('=======================')
        
for l in inp:
    if l == '': continue
    l = l.split(' ')
    printPiles()
    frm, to, qnt = int(l[1]), int(l[3])-1, int(l[5])-1
    move(frm, to, qnt)
# for line in open('in'):
#     if t > 7: break
#     count = 0
#     pile = 0
#     line = line.strip()
#     for char in line:
#         if count == 1 and not char == ' ':
#             print(pile)
#             print(line)
#             piles[pile].append(char) 
#         count+=1
#         if count == 4:
#             count = 0
#             pile += 1
#     t += 1
for p in piles:
    print(p)