import re

pattern = r'mul\(\d+,\s*\d+\)|do\(\)|don\'t\(\)'

tot = 0
do = True
for line in open('in'):
    line = line.strip()
    print(re.findall(pattern, line))
    for mul in re.findall(pattern, line):
        if mul == 'don\'t()':
            print('🚫 STOP')
            do = False
        elif mul == 'do()':
            print('🟢 GO')
            do = True
        else:
            mul = mul[4:-1]
            print(mul)
            if not do:
                continue
            n1, n2 = map(int, mul.split(','))
            tot += n1*n2

print()
print(tot)
        
        