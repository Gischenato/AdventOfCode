data = [tuple(map(int, x.split(','))) for x in open('in').read().strip().split('\n')]

print(data)

acc = 0
biggest = None

def arestas(pontos):
    return [(pontos[i], pontos[(i + 1) % len(pontos)]) for i in range(len(pontos))]

def orientacao(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def ccw(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

def segments_intersect(A, B, C, D):
    o1 = orientacao(A, B, C)
    o2 = orientacao(A, B, D)
    o3 = orientacao(C, D, A)
    o4 = orientacao(C, D, B)

    if o1 * o2 < 0 and o3 * o4 < 0:
        return True

    if o1 == 0 and ponto_em_segmento(A, B, C): return False
    if o2 == 0 and ponto_em_segmento(A, B, D): return False
    if o3 == 0 and ponto_em_segmento(C, D, A): return False
    if o4 == 0 and ponto_em_segmento(C, D, B): return False

    return False

def cria_retangulo(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    left   = min(x1, x2)
    right  = max(x1, x2)
    top    = min(y1, y2)
    bottom = max(y1, y2)

    return [
        (left, top),     # canto superior esquerdo
        (right, top),    # canto superior direito
        (right, bottom), # canto inferior direito
        (left, bottom)   # canto inferior esquerdo
    ]

def ponto_em_segmento(a, b, p):
    (x,y) = p
    (x1,y1) = a
    (x2,y2) = b

    if orientacao(a, b, p) != 0:
        return False

    return (min(x1,x2) <= x <= max(x1,x2) and
            min(y1,y2) <= y <= max(y1,y2))

def dentro_do_poligono(x, y, p):
    ponto = (x,y)

    for i in range(len(p)):
        a = p[i]
        b = p[(i+1) % len(p)]
        if ponto_em_segmento(a, b, ponto):
            return True

    #!Ray casting
    dentro = False
    n = len(p)
    px1, py1 = p[0]

    for i in range(1, n + 1):
        px2, py2 = p[i % n]

        if y > min(py1, py2):
            if y <= max(py1, py2):
                if x <= max(px1, px2):
                    if py1 != py2:
                        xinters = (y - py1) * (px2 - px1) / (py2 - py1) + px1
                    if px1 == px2 or x <= xinters:
                        dentro = not dentro

        px1, py1 = px2, py2

    return dentro

def retangulo_dentro_do_poligono(rect, poly):
    for x, y in rect:
        if not dentro_do_poligono(x, y, poly):
            return False
    
    rect_edges = arestas(rect)
    poly_edges = arestas(poly)

    for r1, r2 in rect_edges:
        for p1, p2 in poly_edges:
            if segments_intersect(r1, r2, p1, p2):
                return False
    
    return True

for i, p1 in enumerate(data):
    print(i, len(data))
    for j, p2 in enumerate(data):
        if j > i:
            rect = cria_retangulo(p1, p2)
            x1,y1 = rect[0]
            x2,y2 = rect[2]
            x_distance = abs(x2 - x1)+1
            y_distance = abs(y2 - y1)+1
            size = x_distance * y_distance
            if not retangulo_dentro_do_poligono(rect, data):
                continue
            if biggest is None or size > biggest:
                print(f"New biggest: {size} from points {p1} and {p2}")
                biggest = size

print(biggest)