start = 50
tot = 0

dial = 50
zeros = 0

for l in open('in'):
    l = l.strip()
    direction = l[0]
    l = l[1:]
    l = int(l)
    if direction == 'L': l = -l

    at_zero = start == 0
    r, start = divmod(start+ l, 100)
    tot += abs(r)
    if l < 0:
        tot += (start == 0) - at_zero



print(tot)