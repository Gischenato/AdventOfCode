arquivo = open('input.txt')

valores = arquivo.readline().split(",")
valores[-1] = '95'
contador = 0

tabelas = []

tabela = []
coluna = 0
for line in arquivo:
     if not line.strip(): continue
     if contador == 5:
          tabelas.append(tabela)
          tabela = []
          contador = 0
          coluna = 0
     linhaList = []
     for valor in line.split():
          linhaList.append({coluna: [valor, False]})
     coluna += 1
     tabela.append(linhaList)
     contador += 1


vetorFinal = []

print(valores)

acabou = False

for num in valores:
     

     for table in tabelas:
          print(table)
          print()
          # break



          # print(table)
          # break
          contador = 0


          for l1, l2, l3, l4, l5 in table:
               if not acabou:
                    for chave, valor in l1.items():
                         if valor[0] == num:
                              l1[chave][1] = True
                    
                    for chave, valor in l2.items():
                         if valor[0] == num:
                              l2[chave][1] = True
                    
                    for chave, valor in l3.items():
                         if valor[0] == num:
                              l3[chave][1] = True

                    for chave, valor in l4.items():
                         if valor[0] == num:
                              l4[chave][1] = True

                    for chave, valor in l5.items():
                         if valor[0] == num:
                              l5[chave][1] = True

               print(f'{ l1} | {l2} | {l3} | {l4} | {l5}')
               

               for c in range(0, 5):
                    contadorL = 0
                    contadorTrues = 0
                    for l in range(0, 5):
                         # print(table[l][c][contadorL][1])

                         if table[l][c][contadorL][1]:
                              contadorTrues += 1
                              if contadorTrues == 5: acabou = True
                         contadorL+=1

               if l1[contador][1] == True and l2[contador][1] == True and l3[contador][1] == True and l4[contador][1] == True and l5[contador][1] == True:
                    acabou = True

               if acabou: print(f'{num} ====')

               if acabou and contador == 4: break

               contador += 1
          # break

          if acabou and contador == 4: break
          print("\n")
          
     if acabou: break
                    # print("ACABOU")
                    # break
               # print(l1)
          
print(len(tabelas))