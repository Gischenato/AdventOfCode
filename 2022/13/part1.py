import json

def compare(val1, val2):
    if isinstance(val1, list) and isinstance(val2, list):
        # print(f'comparing {val1} | {val2}')
        for v1, v2 in zip(val1, val2):
            result = compare(v1, v2)
            # print(f'{val1}/{val2} is: ', result)
            if result == 0 or result == 1: return result
        size1 = len(val1)
        size2 = len(val2)
        if   size1 > size2: return 0
        elif size1 < size2: return 1
        return 2
    elif isinstance(val1, int) and isinstance(val2, int):
        # print(f'comparing {val1} | {val2}')
        if   val1 == val2: return 2
        elif val1 <  val2: return 1
        else: return 0
    else:
        if isinstance(val1, list): return compare(val1, [val2])
        if isinstance(val2, list): return compare([val1], val2)
    pass

current = 1
one, two = [], []
pos = 0
values = []

for line in open('in'):
    if line != '\n':
        if   pos == 0: one = json.loads(line)
        elif pos == 1: two = json.loads(line)
        pos+=1
    elif line == '\n':
        print('#',current)
        # print(one)
        # print(two)
        print('===============')
        ans = compare(one, two)
        if ans == 1: values.append(current)
        if   ans == 0: ans='NOT'
        elif ans == 1: ans='ARE'
        print(f'@@@@@@ {ans} @@@@@@')

        pos = 0 
        current += 1

print('#',current)
# print(one)
# print(two)
ans = compare(one, two)
if   ans == 0: ans='NOT'
elif ans == 1: ans='ARE'
print(f'@@@@@@ {ans} @@@@@@')

print(values)
print(sum(values))