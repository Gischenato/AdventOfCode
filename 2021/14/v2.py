i = 0

insertions = {}
valores = {}
polymeros = {}

for line in open('input.txt'):
     line = line.strip()
     if i == 0:
          template = line
     elif i > 1:
          polymer, pair = line.split(' -> ')
          insertions[polymer] = pair
          polymeros[polymer] = 0
          if pair not in valores.keys():
               valores[pair] = 0
     i += 1

comeco = True
for X in template:
     valores[X] += 1
     if comeco:
          comeco = False 
          anterior = X
          continue
     polymeros[anterior + X] += 1
     anterior = X

for i in range(40):
     novosPolymeros = polymeros.copy()
     for k, v in polymeros.items():
          if v > 0:    
               # print(k,v, insertions[k])
               valores[insertions[k]] += 1 * v
               p0 = k[0]
               p1 = k[1]
               np = insertions[k]
               novosPolymeros[k] -= 1 * v
               novosPolymeros[p0+np] += 1 * v
               novosPolymeros[np+p1] += 1 * v
               # print(p0,p1)

     polymeros = novosPolymeros.copy()

# print(valores)
maior = 0
menor = 1e25
for k, v in valores.items():
     if v > maior: maior = v
     if v < menor: menor = v

print(maior, menor)
print(maior - menor)