
#?   4                     1                     5                        6
#!  100.010.1.00000000001.001|010|1|00000000001|101\010\0\000000000001011\110'100'01111\000\
#*   4   2          1      1   2          1      5   2          11         6   4    15   0
#| SUM = 16

def toInt(binValue):
     return int(binValue, 2)

def getVersion(binario):
     # print(binario)
     version = binario[:3]
     print(version + '.', end ='')
     binario = binario[3:]
     return binario, version

def getType(binario):
     # print(binario)
     type = binario[:3]
     print(type + '.', end ='')
     binario = binario[3:]
     return binario, type


def getLenghtType(binario):
     # print(binario)
     lengthId = binario[0]
     print(lengthId + '.', end ='')
     binario = binario[1:]
     return binario, lengthId

def getSubPacketValue(binario):
     value = binario[:5]
     print(value + '.', end ='')
     continuar = binario[0] == '1'
     binario = binario[5:]

     return binario, value, continuar

def code0(binario):
     value = binario[:15]
     print(value + '.', end ='')
     binario = binario[15:]
     return binario, value

def code1(binario):
     value = binario[:11]
     print(value + '.', end ='')
     binario = binario[11:]
     return binario, value

def getLiteralValue(binario):
     total = 0
     continuar = True
     while continuar:
          binario, value, continuar = getSubPacketValue(binario)
          total += int(value, 2)
     print(" => ", total, end ='')
     return binario, total

def decode(binario):
     global soma
     global total

     if '1' not in binario:
          return
     binario, version = getVersion(binario)
     binario, type = getType(binario)
     # print(toInt(version))
     soma += toInt(version)

     if type == '100':
          binario, litValue = getLiteralValue(binario)
          # return litValue

     elif type:
          binario, lenghtId = getLenghtType(binario)
          binario, value = code0(binario) if lenghtId == '0' else code1(binario)





     print()
     # print(version,type)
     decode(binario)


entrada = '9C0141080250320F1802104A08'
binario = str(bin(int(entrada,16))[2:])
faltando = len(binario) % 4

soma = 0
print(binario)

decode(binario)
print(soma)


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