from collections import deque
N, M = [int(x) for x in input().split()]
visit = [[-1]*M for _ in range(N)] # count
maze = []

def getSurrounderOf(p):
    lst = []
    row, col = p
    #오른쪽과 아래쪽을 먼저 파악한다
    if col + 1 < M:
        if visit[row][col+1]==-1 and maze[row][col+1] == 1:
            lst.append((row, col + 1))
    if row + 1 < N:
        if visit[row+1][col]==-1 and maze[row+1][col] == 1:
            lst.append((row+1, col))
    if row - 1 >= 0:
        if visit[row-1][col]==-1 and maze[row-1][col] == 1:
            lst.append((row-1, col))
    if col - 1 >= 0:
        if visit[row][col-1]==-1 and maze[row][col-1] == 1:
            lst.append((row, col-1))

    return lst


def bfs(v):
    visit[v[0]][v[1]] = 1
    deq = deque([v])

    while deq:
        p = deq.popleft()
        surrounders = getSurrounderOf(p)
        for each in surrounders:
            visit[each[0]][each[1]] = visit[p[0]][p[1]]+1
            deq.append(each)


for _ in range(N):
    line = [int(x) for x in input()]
    maze.append(line)
cnt = []
bfs((0, 0))
print(visit[N-1][M-1])
