sensors = set()
beacons = set()
closest_beacon = dict()
avoid= set()

INPUT = 'in'
POSITION = 2_000_000 if INPUT == 'in' else 10

for line in open('in'):
    line = line.strip().replace(':', '').replace(',', '').split()
    sensorX = int(line[2].split('=')[1])
    sensorY = int(line[3].split('=')[1])
    beaconX = int(line[8].split('=')[1])
    beaconY = int(line[9].split('=')[1])
    sensor = (sensorX, sensorY)
    beacon = (beaconX, beaconY)
    sensors.add(sensor)
    beacons.add(beacon)
    closest_beacon[sensor] = beacon

def find_avoid(sensor):
    global closest_beacon, POSITION, avoid
    beacon = closest_beacon[sensor]
    sensorX, sensorY = sensor
    beaconX, beaconY = beacon

    distance = abs(sensorX - beaconX) + abs(sensorY - beaconY)

    if   sensorY == POSITION:
        for i in range(distance+1):
            avoid.add((sensorX+i,sensorY))
            avoid.add((sensorX-i,sensorY))
    elif sensorY  > POSITION: 
        distanceY = abs(sensorY - POSITION)
        distanceX = distance - distanceY
        for i in range(distanceX+1):
            avoid.add((sensorX+i, sensorY-distanceY))
            avoid.add((sensorX-i, sensorY-distanceY))
    elif sensorY  < POSITION: 
        distanceY = abs(sensorY - POSITION)
        distanceX = distance - distanceY
        for i in range(distanceX+1):
            avoid.add((sensorX+i, sensorY+distanceY))
            avoid.add((sensorX-i, sensorY+distanceY))

def explore():
    for sensor in sensors:
        find_avoid(sensor)


explore()
print(len(avoid.difference(beacons)))