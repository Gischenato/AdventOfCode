from xmlrpc.client import MAXINT
from time import sleep

def isValid(lin, col, maxY, maxX):
     return lin < maxY and lin >= 0 and col < maxX and col >= 0

nodos = dict()
valores = list()

linha = 0
for line in open('in.txt'):
     lin = []
     coluna = 0
     for n in line.strip():
          lin.append(int(n))
          nodos[(linha,coluna)] = int(n)
          coluna += 1
     valores.append(lin)
     linha += 1

tabela = dict()
lista = list(nodos.keys())

print(len(valores))
print(len(valores[0]))

for n in lista:
     tabela[n] = [MAXINT, None]

tabela[(0,0)][0] = 0;

while(len(lista) != 0):
     nodo = lista[0]
     for n in lista:
          if tabela[n][0] < tabela[nodo][0]: nodo = n
     lista.remove(nodo)
     for i in range(-1, 2):
          for j in range(-1, 2):
               if abs(i) == abs(j): continue
               v = (nodo[0]+i, nodo[1]+j)
               if isValid(v[0], v[1], len(valores), len(valores[0])):
                    aux = tabela[nodo][0] + valores[v[0]][v[1]]
                    if aux < tabela[v][0]:
                         tabela[v] = [aux, nodo]
                    

print()
print(tabela[(len(valores)-1, len(valores[0])-1)])
