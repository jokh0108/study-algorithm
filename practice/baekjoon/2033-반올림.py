def getHead(n):
    while n >= 10:
        n = n // 10
    return n

N = int(input())
e = 10
# print()
while True:
    # print(N)
    if N > e:
        h = getHead(N % e)
        if h < 5:
            N = N - h * (e // 10)
        else:
            N = N + (10 - h) * (e // 10)
        e *= 10
    else:
        break
print(N)