def parte1():
     ums = 0
     quadros = 0
     setes = 0
     oitos = 0
     for line in open('in.txt'):
          data, decrypt = line.split('|')
          for string in decrypt.split():
               qnt = len(string)
               if qnt == 2: ums += 1
               elif qnt == 4: quadros += 1
               elif qnt == 3: setes += 1
               elif qnt == 7: oitos += 1

     print(ums + quadros + setes + oitos)

def parte2():
     soma = 0

     for line in open('input.txt'):
          antes, depois = line.split("|")
          antes = [X for X in antes.split()]
          depois = [X for X in depois.split()]

          values = {
               0: set(),
               1: set(list(filter(lambda x: len(x) == 2, antes))[0]),
               2: set(),
               3: set(),
               4: set(list(filter(lambda x: len(x) == 4, antes))[0]),
               5: set(),
               6: set(),
               7: set(list(filter(lambda x: len(x) == 3, antes))[0]),
               8: set(list(filter(lambda x: len(x) == 7, antes))[0]),
               9: set()
          }
          
          display = {
               'A': (values[7]-values[1]).pop(), 
               'B': '',
               'C': '',
               'D': '',
               'E': '',
               'F': '',
               'G': ''

          }

          valores6 = list(filter(lambda x: len(x) == 6, antes))
          valores5 = list(filter(lambda x: len(x) == 5, antes))
          for string in valores6:
               stringSet = set(string)
               if len(stringSet | values[1]) == 7:
                    values[6] = stringSet
               if len(stringSet | values[4]) == 6:
                    values[9] = stringSet
               if len(stringSet | values[4]) == 7 and len(stringSet | values[1]) == 6:
                    values[0] = stringSet


          c = values[1] - values[6]
          f = values[1] - c

          d = values[8] - values[0]
          e = values[8] - values[9]

          g = (values[0] & values[9] & values[6]) - values[1] - values[4] - values[7]

          b = (values[4] - values[1]) & values[0] 


          display['B'] = b.pop()
          display['C'] = c.pop()
          display['D'] = d.pop()
          display['E'] = e.pop()
          display['F'] = f.pop()
          display['G'] = g.pop()

          values[2] = {display['A'], display['C'], display['D'], display['E'], display['G']}
          values[3] = {display['A'], display['C'], display['D'], display['F'], display['G']}
          values[5] = {display['A'], display['B'], display['D'], display['F'], display['G']}

          output = ''
          
          for num in depois:
               num = set(num)
               for key in values:
                    if num == values[key]:
                         output += str(key)

          soma += int(output)
     
     print(soma)



parte2()



#* fbead dcabe bcega gfbecd ecd dgac cd bedcag agebcfd fcagbe | ced cgbefad gbcaef cd
#?   5     3     2      0    7    4   1    9      8      6       7     8       6    1