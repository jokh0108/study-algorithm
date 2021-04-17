N, kim, lim = map(int, input().split())
ROUND = 1
while N != 0:
    # print(ROUND, kim, lim)
    if lim % 2 == 1:
        lim = lim // 2 + 1
    else:
        lim = lim // 2
    if kim % 2 == 1:
        kim = kim // 2 + 1
    else:
        kim = kim // 2

    if lim == kim:
        break
    ROUND += 1

    N = N // 2
print(ROUND)
