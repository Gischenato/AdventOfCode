from typing import Counter
from skimage import io
import numpy as np
import matplotlib.pyplot as plt


vetor2 = np.array([[[
                    int(255/(int(X)+1)) if int(X) != 9 else 0, 
                    int(255/(int(X)+1)) if int(X) != 9 else 0, 
                    int(255/(int(X)+1)) if int(X) != 9 else 0
               ] for X in line.strip()] for line in open('input.txt')])


matrix = [[int(X) for X in line.strip()] for line in open('input.txt')]
posicoesX = [-1, 0, 1, 0]
posicoesY = [0, -1, 0, 1]
rows = len(matrix)
colums = len(matrix[0])

def recriaMatrix():
     global matrix 
     matrix = [[int(X) for X in line.strip()] for line in open('input.txt')]

def show():
     plt.imshow(vetor2)
     plt.show()

cores = [
     [255,255,255],
     [255,0,255],
     [255,255,0],
     [0,255,255],
     [255,0,0],
     [0,255,0],
     [0,0,255],
     [0,104,93],
     [101,22,93],
     [129,76,35],
     [255,155,0],
     [255,121,231],
     [255,0,160],
     [77,255,72],
     [77,45,141],
     [77,0,21],
     [19,87,124]
]

coresIndex = [0]

def validPos(x, y, maxX, maxY):
     return x > -1 and y > -1 and x < maxX and y < maxY

def basin(x, y, colorir = False):
     if matrix[x][y] == 9: return 0

     soma = 1

     for pos in range(4):
          nextRow = x + posicoesX[pos] 
          nextCol = y + posicoesY[pos]
          if validPos(nextRow, nextCol, rows, colums):
               matrix[x][y] = 9
               if colorir == True: vetor2[x][y] = cores[coresIndex[0]]
               soma += basin(nextRow, nextCol, colorir=colorir)
     return soma

def main(colorir = False, colorirMaiores = True, img = False):
     total = 0
     basins = []
     posicoes = []
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
                    if colorir: 
                         val = basin(row, col, colorir=True)
                         coresIndex[0] = coresIndex[0] + 1 if coresIndex[0] < len(cores)-1 else 0

                    else: val = basin(row,col)
                    basins.append(val)
                    posicoes.append((val, (row,col)))

     basins.sort()
     posicoes.sort()
     posicoes = [posicoes[-X] for X in range(1,4)]
     mult = 1
     for i in range(1, 4):
          mult *= basins[-i]

     if colorirMaiores:
          recriaMatrix()
          for val in posicoes:
               basin(val[1][0], val[1][1], colorir=True)
               coresIndex[0] = coresIndex[0] + 1 if coresIndex[0] < len(cores)-1 else 0

     print(total)
     print(mult)

     if img: show()


main(colorir = False, img = True, colorirMaiores=False)