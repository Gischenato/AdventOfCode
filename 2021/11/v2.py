X = [[int(x) for x in line.strip()] for line in open('input.txt')]

pos = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
rows = len(X)
colums = len(X[0])

piscadas = 0

def valid(x, y, maxX = len(X), maxY = len(X[0])) :
     return x > -1 and x < maxX and y > -1 and y < maxY

def piscar(x, y):
     global piscadas
     piscadas += 1
     X[x][y] = 0
     for dx, dy in pos:
          xx = x + dx
          yy = y + dy
          if valid(xx, yy) and X[xx][yy] != 0:
               X[xx][yy] += 1
               if X[xx][yy] >= 10:
                    piscar(xx, yy)

i = 0
while True:
     for row in range(rows):
          for col in range(colums):
               X[row][col] += 1

     for row in range(rows):
          for col in range(colums):
               if X[row][col] > 9:
                    piscar(row, col)

     terinou = True
     for row in range(rows):
          for col in range(colums):
               if X[row][col] != 0: terinou = False

     if terinou:
          print(i + 1) 
          break
     i += 1


print(piscadas)




     

