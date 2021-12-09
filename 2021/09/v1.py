matriz = [[int(y) for y in x.strip()] for x in open('input.txt')]

maiores = []

def basin(i, j):
     soma = 0
     if j == len(matriz[i]): return 0
     if j == -1: return 0
     if i == len(matriz): return 0
     if i == -1: return 
     
     val = matriz[i][j]
     if val == 9: return 0
     else: matriz[i][j] = 9

     if j == 0:
          soma += basin(i, j+1) if matriz[i][j+1] != 9 else 0
          if i == 0:
               soma += basin(i+1, j) if matriz[i+1][j] != 9 else 0
          elif i == len(matriz) - 1:
               soma += basin(i-1, j) if matriz[i-1][j] != 9 else 0
          else:
               soma += basin(i-1, j) if matriz[i-1][j] != 9 else 0
               soma += basin(i+1, j) if matriz[i+1][j] != 9 else 0
     if j == len(matriz[i]) - 1:
          soma += basin(i, j-1) if matriz[i][j-1] != 9 else 0
          if i == 0:
               soma += basin(i+1, j) if matriz[i+1][j] != 9 else 0
          elif i == len(matriz) - 1:
               soma += basin(i-1, j) if matriz[i-1][j] != 9 else 0
          else:
               soma += basin(i-1, j) if matriz[i-1][j] != 9 else 0
               soma += basin(i+1, j) if matriz[i+1][j] != 9 else 0
     else:
          soma += basin(i, j+1) if matriz[i][j+1] != 9 else 0
          soma += basin(i, j-1) if matriz[i][j-1] != 9 else 0
          if i == 0:
               soma += basin(i+1, j) if matriz[i+1][j] != 9 else 0
          elif i == len(matriz) - 1:
               soma += basin(i-1, j) if matriz[i-1][j] != 9 else 0
          else:
               soma += basin(i-1, j) if matriz[i-1][j] != 9 else 0
               soma += basin(i+1, j) if matriz[i+1][j] != 9 else 0
     return soma + 1


def desafio():
     total = 0


     for i in range(len(matriz)):
          for j in range(len(matriz[i])):
               num = matriz[i][j]
               if i == 0:
                    if j == 0 and num < matriz[i+1][j] and num < matriz[i][j+1] : 
                         total += 1 + num
                         maiores.append(basin(i,j))
                    elif j == len(matriz[i]) - 1 and num < matriz[i][j-1] and num < matriz[i+1][j]:
                         total += 1 + num
                         maiores.append(basin(i,j))
                    elif num < matriz[i][j-1] and num < matriz[i+1][j] and num < matriz[i][j+1]:
                         total += 1 + num
                         maiores.append(basin(i,j))
               elif i == len(matriz) - 1:
                    if j == 0 and num < matriz[i-1][j] and num < matriz[i][j+1] : 
                         total += 1 + num
                         maiores.append(basin(i,j))
                    elif j == len(matriz[i]) - 1 and num < matriz[i][j-1] and num < matriz[i-1][j]:
                         total += 1 + num
                         maiores.append(basin(i,j))
                    elif num < matriz[i][j-1] and num < matriz[i-1][j] and num < matriz[i][j+1]:
                         total += 1 + num
                         maiores.append(basin(i,j))
               else:
                    if j == 0 and num < matriz[i][j+1] and num < matriz[i-1][j] and num < matriz[i+1][j]:
                         total += 1 + num
                         maiores.append(basin(i,j))
                    elif j == len(matriz[i]) - 1 and num < matriz[i][j-1] and num < matriz[i-1][j] and num < matriz[i+1][j]:
                         total += 1 + num
                         maiores.append(basin(i,j))
                    elif(not j == len(matriz[i]) - 1):
                         if num < matriz[i][j+1] and num < matriz[i][j-1] and num < matriz[i+1][j] and num < matriz[i-1][j]:
                              total += 1 + num
                              maiores.append(basin(i,j))
     print(total)
     maiores.sort()
     mult = 1
     for i in range(1, 4):
          mult *= maiores[-i]
     print(mult)

desafio()



               