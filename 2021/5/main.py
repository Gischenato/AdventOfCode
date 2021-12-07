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

     x1, x2 = min(x1,x2), max(x1,x2)
     y1, y2 = min(y1,y2), max(y1,y2)

     
     if x1 == x2:
          for y in range(y1 , y2 + 1):
               matriz[x1][y][0] += 1

     if y1 == y2:
          for x in range(x1, x2 + 1):
               matriz[x][y1][0] += 1

qnt = 0

for linha in matriz:
     for value in linha:
          if value[0] > 1: qnt += 1

print(qnt)
