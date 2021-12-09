matrix = [[int(X) for X in line.strip()] for line in open('input.txt')]
posicoesX = [-1, 0, 1, 0]
posicoesY = [0, -1, 0, 1]
rows = len(matrix)
colums = len(matrix[0])


def validPos(x, y, maxX, maxY):
     return x > -1 and y > -1 and x < maxX and y < maxY

def basin(x, y):
     if matrix[x][y] == 9: return 0

     soma = 1

     for pos in range(4):
          nextRow = x + posicoesX[pos] 
          nextCol = y + posicoesY[pos]
          if validPos(nextRow, nextCol, rows, colums):
               matrix[x][y] = 9
               soma += basin(nextRow, nextCol)
     return soma

def main():
     total = 0
     basins = []

     for row in range(rows):
          for col in range(colums):
               menor = True
               for pos in range(4):
                    nextRow = row + posicoesX[pos]
                    nextCol = col + posicoesY[pos]
                    if validPos(nextRow, nextCol, rows, colums):
                         if matrix[nextRow][nextCol] <= matrix[row][col]:
                              menor = False
               if menor:
                    total += 1 + matrix[row][col]
                    basins.append(basin(row, col))

     basins.sort()
     mult = 1
     for i in range(1, 4):
          mult *= basins[-i]

     print(total)
     print(mult)


main()