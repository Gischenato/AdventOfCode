a = open('in')
text = a.read()

passports = text.split('\n\n')


passports = [p.replace('\n', ' ').split(' ') for p in passports]

print(passports[0])


total = 0


def isHexColor(text):
    if text[0] != '#':
        return False
    if len(text) != 7:
        return False
    for c in text[1:]:
        if c not in '0123456789abcdef':
            return False
    return True

def checkDate(text, min, max):
    if len(text) != 4:
        return False
    if not text.isdigit():
        return False
    if not (min <= int(text) <= max):
        return False
    return True

def checkHeight(type, value):
    if type == 'cm':
        if 150 <= int(value) <= 193:
            return True
    elif type == 'in':
        if 59 <= int(value) <= 76:
            return True
    return False 


def checkPassport(p):
    valid = True
    for field in p:
        key, value = field.split(':')
        if key == 'byr':
            if not checkDate(value, 1920, 2002):
                valid = False
                break
        elif key == 'iyr':
            if not checkDate(value, 2010, 2020):
                valid = False
                break
        elif key == 'eyr':
            if not checkDate(value, 2020, 2030):
                valid = False
                break
        elif key == 'hgt':
            if not checkHeight(value[-2:], value[:-2]):
                valid = False
                break
        elif key == 'hcl':
            if not isHexColor(value):
                valid = False
                break
        elif key == 'ecl':
            if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                valid = False
                break
        elif key == 'pid':
            if len(value) != 9:
                valid = False
                break
            if not value.isdigit():
                valid = False
                break
    return valid


for p in passports:
    if len(p) == 8:
        if not checkPassport(p):
            continue
        total += 1
        

    if len(p) == 7:
        cid = False
        for field in p:
            key, value = field.split(':')
            if key == 'cid':
                cid = True
                break
        if not cid and checkPassport(p):
            total += 1

print(total)
        