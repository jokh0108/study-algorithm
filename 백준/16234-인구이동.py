import sys
sys.setrecursionlimit(10**6)

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def dfs(i, j, union):
    global popu
    global cnt
    visited[i][j] = union
    popu += A[i][j]
    cnt += 1
    # print("i, j, cnt, popu: ", i, j, cnt, popu)
    for dr, dc in dirs:
        r, c = i + dr, j + dc
        if 0 <= r < N and 0 <= c < N and visited[r][c] == 0 and L <= abs(A[i][j] - A[r][c]) <= R:
            dfs(r, c, union)

def update_union(data, visited):
    for i in range(N):
        for j in range(N):
            n = visited[i][j]
            if n in data:
                A[i][j] = data[n]

move = 0
while True:
    visited = [[0] * N for _ in range(N)]
    union = 1
    data = {}
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                cnt = 0
                popu = 0
                dfs(i, j, union)
                # print('-------A------', *A, sep='\n')
                # print('-------visited------', *visited, sep='\n')
                # print(cnt, popu)
                if cnt > 1:
                    data[union] = popu // cnt
                union += 1
    
    # print("data", data)
    update_union(data, visited)
    if data:
        move += 1
    else:
        break
    # print('-------A------', *A, sep='\n')

print(move)