from time import sleep
from colorama import Fore, Style

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
     print("\033[2J")
     print('\033[H---MATRIZ---')
     for row in range(rows):
          for col in range(colums):
               val = X[row][col]
               color = Fore.BLACK
               if val == 9 or val == 10: color = Fore.YELLOW 
               print(f'{color}{X[row][col]} {Style.RESET_ALL}', end='')
          print()
     sleep(0.01)

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
          print()


     if terinou:
          print(i + 1) 
          break
     i += 1


print(piscadas)




     

