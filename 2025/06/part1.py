import math
tot = 0

data = []
for line in open('in'):
    print(line.strip().split())
    data.append(line.strip().split())

print(data)
colunas = list(zip(*data))

for c in colunas:
    operacao = c[-1]
    print(operacao)
    if operacao == '+':
        tot += sum(map(int, c[:-1]))
    elif operacao == '*':
        tot += math.prod(map(int, c[:-1]))
        
print(tot)