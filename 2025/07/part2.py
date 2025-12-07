import os
from time import sleep

data = [list(line.strip()) for line in open('in').readlines()]

start = (0, data[0].index('S'))

print(start)

possible_timelines = {}

def is_valid(l,c):
    if l < 0 or c < 0 or l >= len(data) or c >= len(data[0]):
        return False
    return True
tot = 0
to_do = [start]

def add_timeline(l, c, qnt=1):
    if (l,c) not in possible_timelines:
        possible_timelines[(l,c)] = 0
    possible_timelines[(l,c)] += qnt

debug = False

visited = set()

while len(to_do) > 0:
    l,c = to_do.pop(0)
    if (l,c) in visited:
        continue
    visited.add((l,c))
    if debug:
        if input() == 'q':
            debug = False
    if not is_valid(l,c):
        continue
    current_timelines = possible_timelines.get((l,c),1)
    if is_valid(l+1, c):
        next_cell = data[l+1][c]
        
        if next_cell == '.':
            data[l+1][c] = '|'
            add_timeline(l+1, c, current_timelines)
            to_do.append((l+1, c))
        elif next_cell == '^':
            tot += 1
            if is_valid(l+1, c-1):
                data[l+1][c-1] = '|'
                add_timeline(l+1, c-1, current_timelines)
                to_do.append((l+1, c-1))
            if is_valid(l+1, c+1):
                data[l+1][c+1] = '|'
                add_timeline(l+1, c+1, current_timelines)
                to_do.append((l+1, c+1))
        elif next_cell == '|':
            add_timeline(l+1, c, current_timelines)

    if debug:
        data_c = [line.copy() for line in data]
        for key in possible_timelines:
            ll, cc = key
            data_c[ll][cc] = str(possible_timelines[key])
        os.system('cls')
        print('   ' + ' '.join([str(i%10) for i in range(len(data_c[0]))]))
        i = 0
        for line in data_c:
            print(f'{i:2} ', end='')
            for ch in line:
                print(ch, end=' ')
            print()
            i += 1
        print(to_do)
    

last_line_timelines = 0
for key, value in possible_timelines.items():
    l, c = key
    if l == len(data) - 1:
        last_line_timelines += value
        
print(last_line_timelines)