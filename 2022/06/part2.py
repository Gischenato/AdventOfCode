def main():
    val = [line for line in open('in')][0]
    for i in range(len(val)):
        atual = set()
        achou = 0
        for j in range(14):
            if val[i+j] in atual:
                achou = 0
                break
            achou = i+j
            atual.add(val[i+j])
        if achou != 0: 
            print(achou+1)
            break

main()
