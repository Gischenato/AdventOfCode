
def prod(values):
     res = 1
     for v in values:
          res *= v
     return res

def hexToBin(hexValue):
     binValue = ''
     for c in hexValue:
          binValue += f'{int(c, 16):04b}'
     return binValue

def process(binario):
     version = int(binario[:3], 2)
     type = int(binario[3:6], 2)
     if type == 4:
          i = 6
          res = ''
          while True:
               res += binario[i+1 : i+5]
               i += 5
               if binario[i-5] == '0':
                    break
          return version, i, int(res, 2)

     if binario[6] == '0':
          sublen = int(binario[7:22],2)
          values = []
          i = 22
          while i < sublen + 22:
               ver, l, res = process(binario[i:])
               i += l
               version += ver
               values.append(res)
          
     else:
          numpac = int(binario[7:18], 2)
          i = 18
          values = []
          for _ in range(numpac):
               ver, l, res = process(binario[i:])
               version += ver
               i += l
               values.append(res)

     if type == 0:
          res = sum(values)
     elif type == 1:
          res = prod(values)
     elif type == 2:
          res = min(values)
     elif type == 3:
          res = max(values)
     elif type == 5:
          res = int(values[0] > values[1])
     elif type == 6:
          res = int(values[0] < values[1])
     elif type == 7:
          res = int(values[0] == values[1])
     return version, i, res
     

# hexValue = '9C0141080250320F1802104A08'
# binario = hexToBin(hexValue)
# print(process(binario)[2])

inpHexValue = open('input.txt').readline().strip()
inpBinValue = hexToBin(inpHexValue)
verSum, _, res = process(inpBinValue)
print(verSum, res)