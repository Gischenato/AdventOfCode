sensors = set()
closest_beacon = dict()
borders = set()

INPUT = 'in'
MAX = 4_000_000 if INPUT == 'in' else 20

for line in open(INPUT):
    line = line.strip().replace(':', '').replace(',', '').split()
    sensorX = int(line[2].split('=')[1])
    sensorY = int(line[3].split('=')[1])
    beaconX = int(line[8].split('=')[1])
    beaconY = int(line[9].split('=')[1])

    sensor = (sensorX, sensorY)
    beacon = (beaconX, beaconY)
    sensors.add(sensor)
    closest_beacon[sensor] = beacon

def find_borders(sensor):
    global closest_beacon, MAX, borders
    beacon = closest_beacon[sensor]
    sensorX, sensorY = sensor
    beaconX, beaconY = beacon

    distance = abs(sensorX - beaconX) + abs(sensorY - beaconY) + 1
    for i in range(distance+1):
        inBorder = [(sensorX+distance-i, sensorY+i), 
                    (sensorX+distance-i, sensorY-i), 
                    (sensorX-distance+i, sensorY+i), 
                    (sensorX-distance+i, sensorY-i)]
        for border in inBorder:
            if 0 <= border[0] <= MAX and 0 <= border[1] < MAX: borders.add(border)

def explore():
    for sensor in sensors:
        find_borders(sensor)

print('This will take a while...')
explore()
print(f'Total points to check: {len(borders)}')

sensors_distance = dict()
for sensor in sensors:
    beacon = closest_beacon[sensor]
    sensorX, sensorY = sensor
    beaconX, beaconY = beacon

    sensors_distance[sensor] = abs(sensorX - beaconX) + abs(sensorY - beaconY)

testes = 0
for border in borders:
    testes+=1
    if testes % 1_000_000 == 0: print(testes)
    borderX, borderY = border
    dentro = False
    for sensor in sensors:
        if dentro: break
        sensorX, sensorY = sensor
        distance = abs(borderX - sensorX) + abs(borderY - sensorY)
        if distance <= sensors_distance[sensor]: dentro = True
    if not dentro:
        print(f'Find it: {border}')
        print(f'{border[0]} * 4000000 + {border[1]} = {border[0]*4000000+border[1]}')
        break