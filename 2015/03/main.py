dados = list(open('input.txt').read())

def santa():
     X = 0
     Y = 0
     posicoes = set()

     posicoes.add((X,Y))

     for char in dados:
          if char == '>': X += 1
          elif char == '^': Y += 1
          elif char == '<': X -= 1
          elif char == 'v' or char == 'V': Y -= 1

          posicoes.add((X,Y))

     print(len(posicoes))

def robot():
     A = 0
     B = 0
     X = 0
     Y = 0

     posicoes = set()
     
     posicoes.add((0,0))

     contador = 0

     for char in dados:
          santa = True if contador % 2 == 0 else False

          if char == '>': 
               if santa: X += 1 
               else: A += 1
          elif char == '^': 
               if santa: Y += 1
               else: B += 1
          elif char == '<':
               if santa: X -= 1
               else: A -= 1
          elif char == 'v' or char == 'V':
               if santa: Y -= 1
               else: B -= 1

          contador += 1
          posicoes.add((X,Y))
          posicoes.add((A,B))

     print(len(posicoes))


santa()
robot()