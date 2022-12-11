import math

monkeys = {}


def handleOp(monkeyIndex):
    global monkeys
    monkey = monkeys[monkeyIndex]
    monkey['total'] += 1
    new = monkey['itens'].pop(0)
    op = monkey['op'][0]
    qnt = monkey['op'][1]
    if qnt == 'old': qnt = new
    qnt = int(qnt)
    if op == '+':
        new += qnt
    elif op == '-':
        new -= qnt
    elif op == '*':
        new *= qnt
    elif op == '/':
        new/=qnt
    return new

def handleTest(monkeyIndex, new):
    global monkeys
    test = monkeys[monkeyIndex]['test']
    new = math.floor(new/3)
    monkeyTo = -1
    if new % test == 0:
        monkeyTo = monkeys[monkeyIndex]['true']
    else:
        monkeyTo = monkeys[monkeyIndex]['false']
    monkeys[monkeyTo]['itens'].append(new)

current = 0
for line in open('test'):
    line = line.strip().replace(':', '').replace(',', '').split()
    if len(line) == 0: continue
    if line[0] == 'Monkey':
        current = int(line[1])
        monkeys[current] = {
            'itens': [],
            'op': (),
            'test': 0,
            'true': 0,
            'false': 0,
            'total': 0
        }
    elif line[0] == 'Starting':
        monkeys[current]['itens'] = line[2:]
        for i in range(len(monkeys[current]['itens'])):
            monkeys[current]['itens'][i] = int(monkeys[current]['itens'][i])
        pass
    elif line[0] == 'Operation':
        monkeys[current]['op'] = (line[4], line[5])
        pass
    elif line[0] == 'Test':
        monkeys[current]['test'] = int(line[3])
        pass
    elif line[1] == 'true':
        monkeys[current]['true'] = int(line[5])
        pass
    elif line[1] == 'false':
        monkeys[current]['false'] = int(line[5])


for i in range(20):
    for key in monkeys:
        qnt = len(monkeys[key]['itens'])
        for _ in range(qnt):
            handleTest(key, handleOp(key))
    


tot = []
for key in monkeys:
    print(key,monkeys[key])
    tot.append(monkeys[key]['total'])

tot = sorted(tot)
print(tot)
print(tot[-1]*tot[-2])