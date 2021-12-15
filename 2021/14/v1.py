i = 0

insertions = {}

for line in open('input.txt'):
     line = line.strip()
     if i == 0:
          template = line
     elif i > 1:
          polymer, pair = line.split(' -> ')
          insertions[polymer] = pair

     i += 1

template = list(template)

novo = template[:]
for i in range(10):
     i = 1
     novo = template[:]
     comeco = True
     for X in template:
          if comeco:
               comeco = False 
               anterior = X
               continue

          novo.insert(i, insertions[anterior + X])
          anterior = X
          i += 2;
     template = novo[:]

valores = {}

for letra in template:
     if letra not in valores.keys():
          valores[letra] = 0
     else:
          valores[letra] += 1

maior = 0
menor = 1e9

for key in valores:
     if valores[key] > maior: maior = valores[key]
     if valores[key] < menor: menor = valores[key]

print(maior, menor)
print(maior - menor)

