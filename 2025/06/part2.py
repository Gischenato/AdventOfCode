import math
tot = 0

data = []
for line in open('in'):
    data.append(list(line.strip('\n')))
    

colunas = list(zip(*data))

numbers = []
operation = None
for c in colunas:
    if c[-1] in '*+':
        if operation:
            tot += sum(numbers) if operation == '+' else math.prod(numbers)
            numbers = []
        c = list(c)
        operation = c.pop()
    number = ''.join(list(filter(lambda x: x!=' ', c)))
    if number != '':
        numbers.append(int(number))
    
if operation:
    tot += sum(numbers) if operation == '+' else math.prod(numbers)
    numbers = []

print(tot)

