def checkUp(row, col):
    print("checkUp")
    printOffice()
    if office[row][col] == '0':
        office[row][col] = '#'
    if row-1 >= 0:
        temp = office[row-1][col]
        if temp != '#':
            temp = int(temp)
            if 0 <= temp <= 5:
                checkUp(row-1, col)

def checkDown(row, col):
    print("checkDown")
    printOffice()
    global N
    if office[row][col] == '0':
        office[row][col] = '#'
    if row+1 < N:
        temp = office[row+1][col]
        if temp != '#':
            temp = int(temp)
            if 0 <= temp <= 5:
                checkDown(row+1, col)

def checkLeft(row, col):
    print("checkLeft")
    printOffice()
    if office[row][col] == '0':
        office[row][col] = '#'
    if col -1 >= 0:
        temp = office[row][col-1]
        if temp != '#':
            temp = int(temp)
            if 0 <= temp <= 5:
                checkLeft(row, col-1)

def checkRight(row, col):
    print("checkRight")
    printOffice()
    global M
    if office[row][col] == '0':
        office[row][col] = '#'
    if col+1 < M:
        temp = office[row][col+1]
        if temp != '#':
            temp = int(temp)
            if 0 <= temp <= 5:
                checkRight(row, col+1)

def cctv5(row, col):
    checkUp(row, col)
    checkDown(row, col)
    checkLeft(row, col)
    checkRight(row, col)
def cctv1(row, col, n):
    if n == 4:
        checkRight(row, col)
    elif n == 3:
        checkDown(row, col)
    elif n == 2:
        checkLeft(row, col)
    elif n == 1:
        checkUp(row, col)
def cctv2(row, col, n):
    if n == 2:
        checkRight(row, col)
        checkLeft(row, col)
    elif n == 1:
        checkUp(row, col)
        checkDown(row, col)
def cctv3(row, col, n):
    if n == 4:
        checkUp(row, col)
        checkRight(row, col)
    elif n == 3:
        checkRight(row, col)
        checkDown(row, col)
    elif n == 2:
        checkDown(row, col)
        checkLeft(row, col)
    elif n == 1:
        checkLeft(row, col)
        checkUp(row, col)
def cctv4(row, col, n):
    if n == 4:
        checkLeft(row, col)
        checkUp(row, col)
        checkRight(row, col)
    elif n == 3:
        checkUp(row, col)
        checkRight(row, col)
        checkDown(row, col)
    elif n == 2:
        checkRight(row, col)
        checkDown(row, col)
        checkLeft(row, col)
    elif n == 1:
        checkDown(row, col)
        checkLeft(row, col)
        checkUp(row, col)

def printOffice():
    for each in office:
        print(each)
    print()
    


N, M = map(int, input().split())
office = [input().split() for _ in range(N)]
CCTVinfo = {}
for row in range(N):
    for col in range(M):
        cctv = office[row][col]
        if cctv != '#':
            cctv = int(cctv)
            if cctv == 1 or cctv == 3 or cctv ==4:
                CCTVinfo[(cctv, row, col)] = 4               
            elif cctv == 2:
                CCTVinfo[(cctv, row, col)] = 2
            elif cctv == 5:
                cctv5(row, col)
print(CCTVinfo)
while all(CCTVinfo.values()):
    officeCopy = office[:]
    for k, v in CCTVinfo.items():
        if k[0] == 1:
            cctv1(k[1], k[2], v)
        elif k[0] == 2:
            cctv2(k[1], k[2], v)
        elif k[0] == 3:
            cctv3(k[1], k[2], v)
        elif k[0] == 4:
            cctv4(k[1], k[2], v)
        printOffice()
