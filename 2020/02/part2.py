valid = 0

for line in open('in'):
    line = line.strip()
    rule, password = line.split(': ')
    rule_range, rule_letter = rule.split(' ')
    pos1, pos2 = map(int, rule_range.split('-'))
    pos1 = pos1 - 1
    pos2 = pos2 - 1
    inside = False

    if password[pos1] == rule_letter:
        inside = not inside

    if password[pos2] == rule_letter:
        inside = not inside

    if inside:
        valid += 1


print(valid)