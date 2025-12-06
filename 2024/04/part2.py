data = []
for line in open('in'):
    data.append(list(line.strip()))

lines = len(data)
columns = len(data[0])
    
#! Se eu achar M - M -> procurar para cima e para baixo 
#! Se eu achar M -> procurar para esquerda e direita
#!             |
#!             M
#? Ao achar M -> procurar apenas para a direita e para baixo

def is_valid(l, c):
    return 0 <= l < lines and 0 <= c < columns

def look_S_up(l, c):
    if not is_valid(l-1, c+1):
        return 0
    if not data[l-1][c+1] == 'A': return 0
    
    if not is_valid(l-2, c) or not is_valid(l-2, c+2):
        return 0
    if data[l-2][c] == 'S' and data[l-2][c+2] == 'S':
        print("ACHOU X-MAS UP:", (l,c))
        return 1
    return 0

def look_S_down(l, c):
    if not is_valid(l+1, c+1):
        return 0
    if not data[l+1][c+1] == 'A': return 0
    
    if not is_valid(l+2, c) or not is_valid(l+2, c+2):
        return 0
    if data[l+2][c] == 'S' and data[l+2][c+2] == 'S':
        print("ACHOU X-MAS DOWN:", (l,c))
        return 1
    return 0

def look_S_left(l, c):
    if not is_valid(l+1, c-1):
        return 0
    if not data[l+1][c-1] == 'A': return 0
    
    if not is_valid(l, c-2) or not is_valid(l+2, c-2):
        return 0
    if data[l][c-2] == 'S' and data[l+2][c-2] == 'S':
        print("ACHOU X-MAS LEFT:", (l,c))
        return 1
    return 0

def look_S_rigth(l, c):
    if not is_valid(l+1, c+1):
        return 0
    if not data[l+1][c+1] == 'A': return 0
    
    if not is_valid(l, c+2) or not is_valid(l+2, c+2):
        return 0
    if data[l][c+2] == 'S' and data[l+2][c+2] == 'S':
        print("ACHOU X-MAS RIGTH:", (l,c))
        return 1
    return 0

def look_M_rigth(l, c):
    tot = 0
    m_rigth = c + 2
    if is_valid(l, m_rigth):
        if data[l][m_rigth] == 'M':
            tot += look_S_up(l, c)
            tot += look_S_down(l, c)
    return tot
        

def look_M_down(l, c):
    tot = 0
    m_down = l + 2
    if is_valid(m_down, c):
        if data[m_down][c] == 'M':
            tot += look_S_left(l, c)
            tot += look_S_rigth(l, c)
    return tot

def explore():
    tot = 0
    for l in range(lines):
        for c in range(columns):
            if data[l][c] != 'M': continue
            tot += look_M_rigth(l, c)
            tot += look_M_down(l, c)
            
    print("TOTAL:", tot)
explore()

