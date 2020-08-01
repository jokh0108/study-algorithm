from collections import deque
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def get_candidates_and_shark_pos(shark_size):
    lst = []
    for i in range(N):
        for j in range(N):
            # print(333, i, j, board[i][j], board[i][j] != 9 , 0 < board[i][j] < shark_size)
            if board[i][j] != 9 and 0 < board[i][j] < shark_size:
                lst.append((i, j))
            elif board[i][j] == 9:
                y, x = i, j
    return lst, y, x

def bfs(sy, sx, visited, r, c, shark_size):
    d = deque()
    d.append((sy, sx, 0))
    visited[sy][sx] = 99999
    # print(d)

    while d:
        y, x, dist = d.popleft()
        for dy, dx in (-1, 0), (0, -1), (0, 1), (1, 0):
            yy, xx = y+dy, x+dx
            # print(yy, xx)
            if 0<=yy<N and 0<=xx<N :
                if visited[yy][xx] == 0 and board[yy][xx] <= shark_size:
                    visited[yy][xx] = dist + 1
                    if (yy, xx) == (r, c):
                        # print(1111, yy, xx)
                        return visited[yy][xx]
                    # print('---------------- for %d, %d'%(r, c), *visited, sep='\n')
                    d.append((yy, xx, dist+1))
                    # print(d)
    return -1

# print('=============',*board, sep='\n')

import random
N = 20
board = [[random.randint(1, 8) for _ in range(N)] for _ in range(N)]
board[random.randint(0, 19)][random.randint(0, 19)] = 9
print(*board, sep='\n')


def solution():
    shark_size = 2
    time = 0
    ate = 0
    while True:
        candidates, sy, sx = get_candidates_and_shark_pos(shark_size)
        # print("candidates", candidates)
        if not candidates: return time

        arr = []
        for c in candidates:
            visited = [[0]*N for _ in range(N)]
            dist = bfs(sy, sx, visited, *c, shark_size)
            if dist > 0:
                arr.append((c[0], c[1], dist))
        if not arr: return time
        to_be_eaten = sorted(arr, key= lambda x: (x[2], x[0], x[1]))[0]
        syy, sxx, time_passed = to_be_eaten

        board[syy][sxx] = 9
        board[sy][sx] = 0
        ate += 1
        if ate == shark_size:
            ate = 0
            shark_size += 1
        print('=============',*board,shark_size, sep='\n')
        time += time_passed
    

print(solution())