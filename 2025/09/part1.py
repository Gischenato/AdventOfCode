import math

data = [tuple(map(int, x.split(','))) for x in open('in').read().strip().split('\n')]

print(data)

acc = 0
biggest = None

for i, p1 in enumerate(data):
    for j, p2 in enumerate(data):
        if j > i:
            x1,y1 = p1
            x2,y2 = p2
            x_distance = abs(x2 - x1)+1
            y_distance = abs(y2 - y1)+1
            size = x_distance * y_distance
            if biggest is None or size > biggest:
                print(f"New biggest: {size} from points {p1} and {p2}")
                biggest = size

print(biggest)