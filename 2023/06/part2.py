entry = open('in').read().split('\n')

time = entry[0].split(':')[1].strip().split(' ')
distance = entry[1].split(':')[1].strip().split(' ')

empty = time.count('')
for i in range(empty):
    time.remove('')

empty = distance.count('')
for i in range(empty):
    distance.remove('')

join = lambda x: ''.join(x)
time = [join(time)]
distance = [join(distance)]

winners = 0 
for t, d in zip(time, distance):
    for velocity in range(int(t)):
        remaining_time = int(t) - velocity

        if velocity * remaining_time > int(d):
            winners += 1
        
print(winners)