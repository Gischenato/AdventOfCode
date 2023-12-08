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
    # print(origin, rule)
    nodes[origin] = rule
    # break

curr_instruct = 0
curr_node = 'AAA'
while curr_node != 'ZZZ':
    instruct = instructions[curr_instruct % len(instructions)]
    curr_instruct += 1
    # print(curr_node, instruct)
    if instruct == 'L':
        curr_node = nodes[curr_node][0]
    elif instruct == 'R':
        curr_node = nodes[curr_node][1]
    else:
        print('ERROR')
        break

print(curr_instruct)