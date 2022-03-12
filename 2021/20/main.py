arq = open('input.txt')
enhanceAlg = arq.readline().strip()
arq.readline()
matrix = []

for line in arq:
     matrix.append(line.strip())

def printMatrix():
     for l in matrix:
          print(l)
     print()

def valPos(l, c):
     return c >= 0 and c < len(matrix) and l >= 0 and l < len(matrix)

def complement(boll = True):
     comp = '.' if boll else '#'
     for i in range(len(matrix)):
          p = comp
          matrix[i] += comp
          p += matrix[i]
          matrix[i] = p
     tot = len(matrix[0])
     line = comp*tot
     matrix.append(line)
     matrix.insert(0, line)
     # printMatrix()

def getBin(l, c):
     binVal = ''
     for i in range(-1, 2):
          for j in range(-1, 2):
               # print(c+i, ' ', l+j)
               if valPos(l+i, c+j):
                    binVal += '0' if matrix[l+i][c+j] == '.' else '1'
               else: binVal += '0' if matrix[l][c] == '.' else '1'
     return binVal

def enhance(times):
     global matrix
     for t in range(times):
          # complement(True if _ % 2 == 0 else False)
          complement(t%2 == 0)
          newMatrix = []
          for l in range(len(matrix)):
               line = ''
               for c in range(len(matrix)):
                    line += enhanceAlg[int(getBin(l, c), 2)]
               newMatrix.append(line)
          matrix = newMatrix.copy()
     
     tot = 0
     for l in matrix:
          tot += l.count('#')
     printMatrix()
     print(tot)

enhance(50)


