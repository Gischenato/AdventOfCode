faces = dict()

looking_to = [
    (0, 0, .5),
    (0, .5, 0),
    (.5, 0, 0),
    (0, 0, -.5),
    (0, -.5, 0),
    (-.5, 0, 0)
]

for line in open('in'):
    x,y,z = map(int, line.split(','))
    for dX, dY, dZ in looking_to:
        face = (x+dX, y+dY, z+dZ)
        if face not in faces: faces[face] = 1
        else: faces[face] = 0

print(list(faces.values()).count(1))
