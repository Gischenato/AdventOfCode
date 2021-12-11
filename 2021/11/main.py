X = [[int(x) for x in line.strip()] for line in open('input.txt')]

posX = [-1, 0, 1, 0, -1, -1, 1, 1]
posY = [0, -1, 0, 1, -1, 1, -1, 1]
rows = len(X)
colums = len(X[0])

piscadas = 0

def valid(x, y, maxX = len(X), maxY = len(X[0])) :
     return x > -1 and x < maxX and y > -1 and y < maxY

def piscar(x, y):
     global piscadas
     piscadas += 1
     for pos in range(len(posX)):
          row = x + posX[pos]
          col = y + posY[pos]
          if valid(row, col):
               if X[row][col] != 0:
                    X[row][col] += 1

i = 0
while(True):
     posicoes = []

     for row in range(rows):
          for col in range(colums):
               X[row][col] += 1

     continuar = True

     while(continuar):
          continuar = False
          for row in range(rows):
               for col in range(colums):
                    if X[row][col] > 9:
                         posicoes.append((row,col))
                         piscar(row, col)
                    if X[row][col] > 9:
                         X[row][col] = 0
                    
          for row in range(rows):
               for col in range(colums):
                    if X[row][col] > 9:
                         continuar = True

     terinou = True
     for row in range(rows):
          for col in range(colums):
               if X[row][col] != 0: terinou = False
               
     if terinou:
          print(i + 1) 
          break
     i += 1


print(piscadas)




     

