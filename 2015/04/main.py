import hashlib


inp = 'ckczppom'

contador = 1

while(True):
     key = inp + str(contador)
     if hashlib.md5(key.encode()).hexdigest().startswith('0000000'):
          print(key)
          print(contador)
          break
     contador += 1





