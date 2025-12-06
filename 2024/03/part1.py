# def get_next_mult(line, acc=0):
import re

pattern = r'mul\(\d+,\s*\d+\)'
tot = 0
for line in open('ex'):
    line = line.strip()
    print(re.findall(pattern, line))
    for mul in re.findall(pattern, line):
        mul = mul[4:-1]
        print(mul)
        n1, n2 = map(int, mul.split(','))
        tot += n1*n2
print(tot)
        
        
        