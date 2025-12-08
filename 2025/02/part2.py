data = open('in').readline().strip().split(',')

total_ids = 0

for r in data:
    start, end = map(int, r.split('-'))
    i = start - 1
    
    while i < end:
        i += 1
        s = str(i)
        n = len(s)

        divisores = [d for d in range(2, n + 1) if n % d == 0]

        find_one = False
        for v in divisores:
            size = n // v
            parts = [s[x*size:(x+1)*size] for x in range(v)]

            if len(set(parts)) == 1:
                print(i, parts)
                total_ids+=i
                break

print(total_ids)