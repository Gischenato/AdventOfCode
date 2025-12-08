data = open('in').readline().strip().split(',')

total_ids = 0

for r in data:
    start, end = map(int, r.split('-'))
    i = int(start)-1
    while i < end:
        i += 1
        s = str(i)
        if len(s) % 2 == 1: continue
        size = int(len(s)/2)
        s1 = s[0:size]
        s2 = s[size:]
        if s1 == s2:
            print(i)
            print('FIND IT')
            total_ids += i

print(total_ids)
