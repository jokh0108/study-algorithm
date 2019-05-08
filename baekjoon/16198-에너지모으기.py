from collections import deque

def getEnergy(e, result):
    global M
    if len(e) == 2:
        # print(result)
        if M < result:
            M = result
        return 0
    for i in range(1, len(e)-1):
        c = e.copy()
        result += c[i-1]*c[i+1]
        del c[i]
        # print(c)
        # print(result)
        getEnergy(c, result)
        result -= c[i-1]*c[i]
    
input()
e = deque([int(x) for x in input().split()])
M = -999999999
for i in range(1, len(e)-1):
    c = e.copy()
    result = c[i-1]*c[i+1]
    del c[i]
    # print(c)
    # print(result)
    getEnergy(c, result)
    result -= c[i-1]*c[i]
    
# print(e)
print(M)