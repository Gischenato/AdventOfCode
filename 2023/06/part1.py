entry = open('in').read().split('\n')

time = entry[0].split(':')[1].strip().split(' ')
distance = entry[1].split(':')[1].strip().split(' ')

empty = time.count('')
for i in range(empty):
    time.remove('')

empty = distance.count('')
for i in range(empty):
    distance.remove('')

tot = 1
for t, d in zip(time, distance):
    winners = 0
    for velocity in range(int(t)):
        remaining_time = int(t) - velocity

        if velocity * remaining_time > int(d):
            winners += 1

    if winners == 0:
        winners = 1
    tot *= winners

print(tot)