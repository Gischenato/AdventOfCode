maiorX = 0
maiorY = 0
for line in open("input.txt"):
     dados = line.split('->')
     dados[1] = dados[1].strip()
     dados = dados[0].split(',') + dados[1].split(',')

     for a, b in enumerate(dados):
          if a % 2 == 0:
               maiorX = b if int(b) > int(maiorX) else maiorX
          else:
               maiorY = b if int(b) > int(maiorY) else maiorY

maiorX = int(maiorX)
maiorY = int(maiorY)

matriz = [[[int(0)] for j in range(maiorY + 1)] for i in range(maiorX + 1)]

for line in open("input.txt"):
     dados = line.split('->')
     dados[1] = dados[1].strip()
     dados = dados[0].split(',') + dados[1].split(',')

     x1 = int(dados[0])
     x2 = int(dados[2])

     y1 = int(dados[1])
     y2 = int(dados[3])

     dx = x2 - x1
     dy = y2 - y1

     for pos in range(1 + max(abs(dx),abs(dy))):
          posX = pos if dx > 0 else -pos
          posX = 0 if dx == 0 else posX

          posY = pos if dy > 0 else -pos
          posY = 0 if dy == 0 else posY
          
          matriz[x1 + posX][y1 + posY][0] += 1

     
qnt = 0

for linha in matriz:
     for value in linha:
          if value[0] > 1: qnt += 1

print(qnt)
