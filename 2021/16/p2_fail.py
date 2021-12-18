def toInt(binValue):
     return int(binValue, 2)

def graterThan(val1, val2):
     return 1 if val1 > val2 else 0

def lessThen(val1, val2):
     return 1 if val1 < val2 else 0

def equal(val1, val2):
     return 1 if val1 == val2 else 0

def getVersion():
     global binario
     version = binario[:3]
     binario = binario[3:]
     return version

def getType():
     global binario
     type = binario[:3]
     binario = binario[3:]
     return type


def getLenghtType():
     global binario
     lengthId = binario[0]
     binario = binario[1:]
     return lengthId

def getSubPacketValue():
     global binario
     value = binario[1:5]
     continuar = binario[0] == '1'
     binario = binario[5:]

     return value, continuar

def code0():
     global binario
     value = binario[:15]
     binario = binario[15:]
     return value

def code1():
     global binario
     value = binario[:11]
     binario = binario[11:]
     return value

def getLiteralValue():
     global binario
     total = ''
     continuar = True
     while continuar:
          value, continuar = getSubPacketValue()
          total += value
     return int(total, 2)


def contarPacotes(val):
     newBin = binario[:val]
     total = 0
     while newBin:
          ver = newBin[:3]
          type = newBin[3:6]
          newBin = newBin[6:]
          if type == '100':
               continuar = True
               while continuar:
                    continuar = newBin[0] == '1'
                    newBin = newBin[5:]
          else:
               length = newBin[0]
               newBin = newBin[1:]
               if length == '1':
                    newBin = newBin[11:]
               if length == '0':
                    newBin = newBin[15:]
          total += 1
     return total



def decode():
     global binario
     if '1' not in binario:
          print("ENTREI AQUI")
          return 
     version = getVersion()
     type = getType()
     print(binario, '\n')
     if type == '100':
          litValue = getLiteralValue()
          return litValue
     else:
          lenghtId = getLenghtType()
          value = code0() if lenghtId == '0' else code1()
          value = int(value, 2) 
          if lenghtId == '0': value = contarPacotes(value)

          if type == '000':
               soma = 0
               for i in range(value):
                    soma += decode()
               return soma
               
          elif type == '001':
               produto = 1
               for i in range(value):
                    produto *= decode()
               return produto
               
          elif type == '010':
               minimo = 1e9
               for i in range(value):
                    val = decode()
                    if minimo > val: minimo = val
               
               return minimo
               
          elif type == '011':
               maximo = 0
               for i in range(value):
                    val = decode()
                    if val > maximo: maximo = val

               return maximo
               
          elif type == '101':
               return graterThan(decode(), decode())
               
          elif type == '110':
               return lessThen(decode(), decode())
               
          elif type == '111':
               return equal(decode(), decode())
          else: 
               print("BADVIBES")

def hexToBin(hexValue):
     binValue = ''
     for c in hexValue:
          binValue += f'{int(c, 16):04b}'
     return binValue       

entrada = 'D8005AC2A8F0'
binario = hexToBin(entrada)
faltando = len(binario) % 4

print(binario)

print("\n!!!", decode())


#|    100.111.0.            EQUALS   1 + 3 == 2 * 2 -> True
#|    000000001010000.
#|         010.000.1.       SOMAR    1 + 3
#|         00000000010.
#|               010.100.00001.
#|               100.100.00011.
#|         110.001.1.       PRODUTO   
#|         00000000010.              2 * 2
#|               000.100.00010.
#|               010.100.00010.
#|    00