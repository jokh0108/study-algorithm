import pprint

t = int(input())
MAX = 71
bino = [[0 for _ in range(MAX)] for _ in range(MAX)]

for i in range(MAX):
    bino[i][0] = 1
    bino[i][i] = 1

for n in range(2, MAX):
    for r in range(1, n):
        bino[n][r] = bino[n-1][r-1] + bino[n-1][r]

# pprint.pprint(bino, width=120, compact=True)

for j in range(t):
    n, a, b = map(int, input().split())
    print("#%d"%(j+1), bino[n][a])



