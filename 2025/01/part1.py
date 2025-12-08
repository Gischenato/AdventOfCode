start = 50
tot = 0

for l in open('in'):
    l = l.strip()
    direction = l[0]
    l = l[1:]
    l = int(l)
    if direction == 'L': l = -l

    r, start = divmod(start+ l, 100)
    if start == 0:
        tot+=1

print(tot)
