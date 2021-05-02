T = int(input())


d = [[0, 0] for _ in range(42)]
d[0], d[1] = [1, 0], [0, 1]
for i in range(2, 42):
    d[i] = [d[i - 1][0] + d[i - 2][0], d[i - 1][1] + d[i - 2][1]]

for _ in range(T):
    N = int(input())
    print(*d[N], sep=" ")
