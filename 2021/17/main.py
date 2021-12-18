data = open('input.txt').readline().strip().replace(',', '').replace('=', ' ').split()

xi, xf = data[3].split('..')
yi, yf = data[5].split('..')


xi = int(xi)
xf = int(xf)
yi = int(yi)
yf = int(yf)


coords = {
     'xi': xi,
     'xf': xf,
     'yi': yi,
     'yf': yf
}

def checkIfInArea(x, y):
     return x >= coords['xi'] and x <= coords['xf'] and y >= coords['yi'] and y <= coords['yf']

def failed(x,y):
     return x > coords['xf'] or y < coords['yi']


ySpeeds = []
coordsValues = []

menor = True
X = 0
Y = 0

maiorY = 0

for X in range(1000):
     for Y in range(-100, 1000):
               x = 0
               y = 0

               initXSpeed = X
               initYSpeed = Y

               yTrajectory = []

               ySpeed = initYSpeed
               xSpeed = initXSpeed

               while True:
                    if failed(x,y):
                         break
                    x += xSpeed
                    y += ySpeed
                    xSpeed = xSpeed - 1 if xSpeed > 0 else xSpeed
                    ySpeed -= 1
                    yTrajectory.append(y)
                    if checkIfInArea(x,y):
                         coordsValues.append((initXSpeed, initYSpeed))
                         if max(yTrajectory) > maiorY:
                              maiorY = max(yTrajectory)
                              # print(maiorY, (initXSpeed, initYSpeed)) 
                         ySpeeds.append(initYSpeed)
                         break

print('Parte 1: ', maiorY)
print('Parte 2: ', len(coordsValues))