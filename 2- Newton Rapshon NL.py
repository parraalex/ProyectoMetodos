def createMatriz(m,n,v):
    C = []
    for i in range(m):
        C.append([])
        for j in range(n):
            C[i].append(v)
    return C

def getDimensiones(A):
    return(len(A), len(A[0]))

def sumMatrices(A,B):
    Am,An = getDimensiones(A)
    Bm,Bn = getDimensiones(B)
    if Am != Bm or An!= Bn:
        print("Las dimensiones son diferentes")
        return[]
    C = createMatriz(Am,An,0)
    for i in range(Am):
        for j in range(An):
            C[i][j] = A[i][j] + B[i][j]
    return C

def mulMatrices(A,B):
    Am,An = getDimensiones(A)
    Bm,Bn = getDimensiones(B)
    if An != Bm:
        print("Las matrices no son conformables")
        return []
    C = createMatriz(Am,Bn,0)
    for i in range(Am):
        for j in range(Bn):
            for k in range(An):
                C[i][j] += A[i][k] * B[k][j]
    return C

def getMenorMatriz(A,r,c):
    m,n = getDimensiones(A)
    C = createMatriz(m-1,n-1,0)
    for i in range (m):
        if i == r:
            continue
        for j in range(n):
            if j == c:
                continue
            Ci = i
            if i > r:
                   Ci = i-1
            Cj = j
            if j > c:
                Cj = j-1
            C[Ci][Cj] = A[i][j]


    return C

def detMatriz(A):
    m,n = getDimensiones(A)
    if m != n:
        print("La matriz no es cuadrada")
        return -1
    if m == 1:
        return m
    if m == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    det = 0
    for j in range(n):
        det += (-1)**(j)*A[0][j]*detMatriz(getMenorMatriz(A,0,j))
    return det


def getMatrizAdyacente(A):
    m,n = getDimensiones(A)
    C = createMatriz(m,n,0)
    for i in range(m):
        for j in range(n):
            C[i][j] = (-1)**(i+j)*detMatriz(getMenorMatriz(A,i,j))
    return C


def getMatrizTranspuesta(A):
    m,n = getDimensiones(A)
    C = createMatriz(n,m,0)
    for i in range(m):
        for j in range(n):
            C[j][i] = A[i][j]
    return C


def getMatrizInversa(A):
    detA = detMatriz(A)
    if detA == 0:
        print("La matriz no tiene inversa")
        return 0
    At = getMatrizTranspuesta(A)
    adyAt = getMatrizAdyacente(At)
    m,n = getDimensiones(A)
    C = createMatriz(m,n,0)
    for i in range(m):
        for j in range(n):
            C[i][j] = (1/detA)*adyAt[i][j]
    return C


# ejemplo
# x^2 + y^2 = 10 -> u
# x^2 - y^2 = 1 -> v

def duDX(x):
    return 2*x

def duDY(y):
    return 2*y

def dvDX(x):
    return 2*x

def dvDY(y):
    return -2*y

def u(x,y):
    return x**2 + y**2 - 10

def v(x,y):
    return x**2 - y**2 - 1

A = [[duDX,duDY],[dvDX,dvDY]]
C = [[u],[v]]

x0 = 1
y0 = 1
E = 0.01

for i in range(100):
    Ai = createMatrix(2,2,0)
    Ain,Aim = getDimensions(Ai)
    for k in range(Ain):
        for j in range(Aim):
            Ai[k][j] = Ai[k][j](x0,y0)
    print(Ai)
    Ainv = getMatrizInversa(Ai)
    print(Ainv)
    Ci = createMatrix(2,1,0)
    for k in range(2):
        Ci[k][0] = C[k][0](x0,y0)
    
    
