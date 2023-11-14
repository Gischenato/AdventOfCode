valid = 0

for line in open('in'):
    line = line.strip()
    rule, password = line.split(': ')
    rule_range, rule_letter = rule.split(' ')
    minimum, maximum = map(int, rule_range.split('-'))

    counter = 0
    for l in password:
        if l == rule_letter:
            counter += 1
    
    if minimum <= counter <= maximum: 
        valid += 1

print(valid)