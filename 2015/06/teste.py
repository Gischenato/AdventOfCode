def parte1():
     grid = [[False for i in range(1000)] for x in range(1000)]

     for line in open('input.txt'):
          dados = line.split()
          x1, y1 = dados[-3].split(',')
          x2, y2 = dados[-1].split(',')
          
          x1, x2 = int(x1), int(x2)  
          y1, y2 = int(y1), int(y2)


          for x in range(x1, x2+1):
               for y in range(y1, y2+1):
                    if dados[0] == 'toggle':
                         grid[x][y] = False if grid[x][y] else True
                    elif dados[1] == 'on':
                         grid[x][y] = True
                    elif dados[1] == 'off':
                         grid[x][y] = False

     total = 0

     for x in range(1000):
          for y in range(1000):
               total += 1 if grid[x][y] else 0
          
          if x % 10 == 0: print

     print(total)

def parte2():
     grid = [[0 for i in range(1000)] for x in range(1000)]
     total = 0

     for line in open('input.txt'):
          dados = line.split()
          x1, y1 = dados[-3].split(',')
          x2, y2 = dados[-1].split(',')
          
          x1, x2 = int(x1), int(x2)  
          y1, y2 = int(y1), int(y2)

          for x in range(x1, x2+1):
               for y in range(y1, y2+1):
                    if dados[0] == 'toggle':
                         grid[x][y] += 2
                    elif dados[1] == 'on':
                         grid[x][y] += 1
                    elif dados[1] == 'off':
                         grid[x][y] -= 1 if grid[x][y] > 0 else 0
                         


     total += sum(sum(coluna) for coluna in grid)

     print(total)


parte2()
parte1()