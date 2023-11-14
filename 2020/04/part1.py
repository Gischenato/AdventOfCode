a = open('in')
text = a.read()

passports = text.split('\n\n')


passports = [p.replace('\n', ' ').split(' ') for p in passports]

print(passports[0])


total = 0

for p in passports:
    if len(p) == 8:
        total += 1
        continue

    if len(p) == 7:
        cid = False
        for field in p:
            key, value = field.split(':')
            if key == 'cid':
                cid = True
                break
        if not cid:
            total += 1

print(total)
        