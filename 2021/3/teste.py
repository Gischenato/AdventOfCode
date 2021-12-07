bits = []
for linha in open('input.txt'):
    linha = linha.strip()
    bits.append(linha)

tamanho = 12

oxygen = list(bits)
co2 = list(bits)

for i in range(tamanho):
    if len(oxygen) > 1:
        zerosO2 = len([x  for x in oxygen if x[i]=='0'])
        ums02 = len([x  for x in oxygen if x[i]=='1'])
        if ums02 >= zerosO2:
            oxygen = [x for x in oxygen if x[i]=='1']
        else:
            oxygen = [x for x in oxygen if x[i]=='0']

    if len(co2) > 1:
        zerosCO2 = len([x  for x in co2 if x[i]=='0'])
        umsCO2 = len([x  for x in co2 if x[i]=='1'])
        if zerosCO2 >= umsCO2:
            co2 = [x for x in co2 if x[i]=='0']
        else:
            co2 = [x for x in co2 if x[i]=='1']
print(int(oxygen[0]), " ", int(co2[0]))