def is_biggest(a, b):
    return int(a) > int(b)

tot = 0
for line in open('in'):
    biggest_number = 0
    line = line.strip()
    biggest = line[0]
    line = line[1:]


    for c in line:
        new_number = int(biggest + c)
        if is_biggest(new_number, biggest_number):
            biggest_number = new_number
        if is_biggest(c, biggest):
            biggest = c
    tot += biggest_number
    print(biggest_number)

print(tot)
