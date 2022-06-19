from time import sleep

def putMap():
     RESET = '\033[m'
     RED = '\033[31m'
     GREEN = '\033[32m'
     BLUE = '\033[34m'
     print('\033[2J')
     print('\033[H')
     print(' ', end = '')
     print()
     i = 0
     for l in mapa:
          for c in l:
               if c == 'G':
                    print(f'{GREEN}{c}{RESET}', end = '')
               elif c == 'E':
                    print(f'{BLUE}{c}{RESET}', end = '')
               elif c == '#':
                    print(f'{RED}{c}{RESET}', end = '')
               else:
                    print(c, end ='')
          print()
          i += 1

def isValid(pos):
     x = pos[0]
     y = pos[1]
     return x >= 0 and y >= 0 and x < MAXX and y < MAXY

def poeEmOrdem(lista):
     return sorted(lista, key=lambda x: x['pos'][1]*MAXX+x['pos'][0])


def naoFaz(ent):
     a = ent['pos']
     i = ent['id']
     for aa in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
          aX = a[0]+aa[0]
          aY = a[1]+aa[1]
          if mapa[aY][aX] == 'G' and mapa[a[1]][a[0]] == 'E':
               return True
          if mapa[aY][aX] == 'E' and mapa[a[1]][a[0]] == 'G':
               return True
     return False

def vivos():
     print("GOBLINS: ", end = '')
     for e in entity:
          if e['id'] == 'G':
               print(e['vida'], end=' | ')
     print("\nELFOS: ", end = '  ')
     for e in entity:
          if e['id'] == 'E':
               print(e['vida'], end=' | ')
     print()
     for i in entity:
          print(i['pos'], end = '|')
     
     print()

def ataca(ent, entidades):
     a = ent['pos']
     i = ent['id']
     adjacentes = []

     achou = False
     for aa in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
          aX = a[0]+aa[0]
          aY = a[1]+aa[1]
          if mapa[aY][aX] == 'G' and mapa[a[1]][a[0]] == 'E':
               adjacentes.append((aX, aY))
               achou = True
          if mapa[aY][aX] == 'E' and mapa[a[1]][a[0]] == 'G':
               adjacentes.append((aX, aY))
               achou = True
     # print(adjacentes)
     if achou:
          vidas = sorted(entidades, key= lambda x: x['vida'])
          for e in vidas:
               # if e['vida'] <= 0: continue
               for i in adjacentes:
                    if e['pos'] == i:
                         e['vida'] = e['vida'] - ent['dano']
                         # print(adjacentes, individuo)
                         # print(f'{ent} -> {e}')
                         # sleep(1)
                         if e['vida'] <= 0:
                              # entidades.remove(e)
                              a = e['pos']
                              mapa[a[1]][a[0]] = '.'
                              return e
                         return ent
     return ent

INPUT = 'input.txt'
TIME = .05
imprimir = True
dano = 3

for i in range(100):
     a = 0
     elfoMorto = False


     mapa = []
     elvs = []
     goblins = []
     entity = []
     contadorG = 0
     contadorE = 0

     l = 0
     for line in open(INPUT):
          lin = []
          c = 0
          for char in line.strip():
               if char == 'G':
                    contadorG += 1
                    goblins.append(((c, l), 200))
               elif char == 'E':
                    contadorE += 1
                    elvs.append(((c, l), 200))
               if char == 'G' or char == 'E':
                    entity.append({
                         'pos': (c,l),
                         'vida': 200,
                         'id': char,
                         'dano': 3 if char == 'G' else dano
                    })
               lin.append(char)
               c += 1
          mapa.append(lin)
          l += 1

     MAXX = len(mapa[0])
     MAXY = len(mapa)

     if imprimir:
          putMap()     
          print()
          vivos()
          print()

     while True:
          # input()
          entity = poeEmOrdem(entity)
          # if a >21:
          #      input()
          contadorG = 0
          contadorE = 0
          for i in entity:
               if i['id'] == 'G': contadorG += 1
               if i['id'] == 'E': contadorE += 1
          if contadorE == 0 or contadorG == 0: break
          a += 1

          
         
          mortos = []
          for z in range(len(entity)):
               if z >= len(entity): continue
               e = entity[z]
               if e['vida'] <= 0: continue
               if naoFaz(e):
                    lp = ataca(e, entity)
                    if not lp['pos'] == e['pos']:
                         mortos.append(lp)
                    # sleep(TIME)
                    # putMap()
                    # print()
                    # vivos()
                    # print(a)
                    continue

               posI = e['pos']
               marcados = set([posI])
               explorar = [(posI, [])]
               encontrou = False
               while len(explorar) != 0:
                    # print("aqui")
                    v = explorar.pop(0)
                    posE = v[0]
                    for p in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                         pos = (posE[0]+p[0], posE[1]+p[1])
                         if not isValid(pos): continue
                         if pos in marcados or mapa[pos[1]][pos[0]] == '#': continue
                         marcados.add(pos)
                         if mapa[pos[1]][pos[0]] == '.':
                              aux = v[1].copy()
                              aux.append(pos)
                              explorar.append((pos, aux))
                         elif mapa[pos[1]][pos[0]] == 'G' and e['id'] == 'E':
                              explorar = []
                              encontrou = True
                              break
                         elif mapa[pos[1]][pos[0]] == 'E'  and e['id'] == 'G':
                              explorar = []
                              encontrou = True
                              break
          
               if encontrou:
                    if len(v[1]) > 0:
                         mapa[posI[1]][posI[0]] = '.'
                         p = v[1][0]
                         mapa[p[1]][p[0]] = e['id']
                    entity[z]['pos'] = p
               
               # ataca(e, entity)
               lp = ataca(e, entity)
               if not lp['pos'] == e['pos']:
                    mortos.append(lp)
          for m in mortos:
               if m in entity:
                    if m['id'] == 'E':
                         elfoMorto = True
                    entity.remove(m)
          if elfoMorto: break
          # input()
          if imprimir:
               sleep(TIME)
               putMap()
               print()
               vivos()
               print(a)
               print(dano)



     print()
     t = 0
     for e in entity:
          t += e['vida']
     a -= 1
     # print(a)
     # print(t)
     # print(a * t)

     if not elfoMorto:
          print('acabou!!!')
          print(a, '*', t)
          print(a*t)
          print(dano)
          break
     dano += 1
     # sleep(1)

# 58 1178