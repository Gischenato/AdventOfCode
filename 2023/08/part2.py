start = True

instructions = ''

nodes = {}

for line in open('in'):
    line = line.strip()
    if start:
        print(line)
        instructions = line
        start = False
        continue
    if line == '': continue
    origin, rule = line.split(' = ')
    rule = rule.replace('(', '').replace(')', '').split(', ')
    nodes[origin] = rule

to_start = [x if x.endswith('A') else None for x in nodes.keys()]
to_start = list(set(to_start))
to_start.remove(None)


find = {}
for i in range(len(to_start)):
    find[i] = [0, False]

print(find)

print(to_start)

def lcm_multiple(numbers):
    def lcm(x, y):
        maior = max(x, y)

        multiplo = maior

        while True:
            if multiplo % x == 0 and multiplo % y == 0:
                return multiplo
            multiplo += maior

    resultado = numbers[0]
    for i in range(1, len(numbers)):
        resultado = lcm(resultado, numbers[i])

    return resultado

curr_instruct = 0
while True:
    if not False in [x[1] for x in find.values()]:
        print('='*45)
        break

    instruct = 0 if instructions[curr_instruct % len(instructions)] == 'L' else 1

    for i in range(len(to_start)):
        node = to_start[i]
        to_start[i] = nodes[node][instruct]
        if not find[i][1]:
            find[i][0] += 1
        if to_start[i].endswith('Z'):
            find[i][1] = True

    print(to_start, curr_instruct, find)
    curr_instruct += 1

values = [x[0] for x in find.values()]
print(values)
print(f'lcm: {lcm_multiple(values)}')
