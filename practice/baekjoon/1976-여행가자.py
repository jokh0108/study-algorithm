def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        root[y] = x
    else:
        root[x] = y

N = int(input())
M = int(input())
root = [i for i in range(N)]
board = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(lambda x: int(x)-1, input().split()))
# print(*board, sep='\n')

for i in range(N):
    for j in range(N):
        if board[i][j]:
            union(i, j)
# print(root)

arr = []
for city in plan:
    arr.append(root[city])
if len(set(arr)) == 1:
    print('YES')
else:
    print('NO')
