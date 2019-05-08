import sys
sys.setrecursionlimit(15000)
def dfs(i, j, N, color):
    visited[i][j] = True

    if i-1 >= 0:
        if img[i-1][j] == color and not visited[i-1][j]:
            dfs(i-1, j, N, color)
    if j-1 >= 0:
        if img[i][j-1] == color and not visited[i][j-1]:
            dfs(i, j-1, N, color)
    if i+1 < N:
        if img[i+1][j] == color and not visited[i+1][j]:
            dfs(i+1, j, N, color)
    if j+1 < N:
        if img[i][j+1] == color and not visited[i][j+1]:
            dfs(i, j+1, N, color)


N = int(input())
# RGB
img = []
for _ in range(N):
    img.append(list(input()))

visited = [[False]*N for _ in range(N)]
cntRGB = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, N, img[i][j])
            cntRGB += 1
# RRB
for i in range(N):
    for j in range(N):
        if img[i][j] == 'G':
            img[i][j] = 'R'
visited = [[False]*N for _ in range(N)]
cntRRB = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, N, img[i][j])
            cntRRB += 1
print(cntRGB, cntRRB)
