def parte1():
     nice = 0
     for line in open('input.txt'):
          vogais = 0
          twices = False
          errado = True

          aux = ''

          chars = list(line.strip())

          for char in chars:
               if char in 'aeiou': vogais += 1
               if char == aux: twices = True
               notString = aux + char
               if notString == 'ab' or notString == 'cd' or notString == 'pq' or notString == 'xy': errado = False

               aux = char
          if vogais >= 3 and twices and errado: nice += 1

     print(nice)


def parte2():
     nice = 0
     for line in open('input.txt'):
          twos = set()
          containsTwo = False
          repetidos = []
          repeats = False


          aux1 = ''
          aux2 = ''

          chars = list(line.strip())

          pegar = False

          for char in chars:
               if not char == aux1 == aux2:
                    if(aux1 + char) in twos:
                         containsTwo = True
                         repetidos.append(aux1 + char)
                    twos.add(aux1 + char)

               
               if aux2 == char: 
                    repeats = True

               if pegar: aux2 = aux1
               pegar = True
               aux1 = char

          if containsTwo and repeats: nice += 1

     print(nice)

parte2()
