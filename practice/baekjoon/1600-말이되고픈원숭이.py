from collections import deque

k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
# print(*board, sep='\n')

dd = [(-1, 0), (0, -1), (0, +1), (+1, 0)]
dh = [(-1, -2), (-2, -1), (-2, +1), (-1, +2),
      (+1, +2), (+2, +1), (+2, -1), (+1, -2)]


def bfs(x, y, lv):
    global k
    q = deque()
    board[x][y] = lv
    q.append((x, y, lv))
    while q:
        xx, yy, lv = q.popleft()
        board[xx][yy] = lv
        # print(*board, '-'*10, sep='\n')
        for dx, dy in dd:
            xxx, yyy = xx + dx, yy + dy
            if (0 <= xxx < h and 0 <= yyy < w ) and (not board[xxx][yyy] or lv < board[xxx][yyy]):
                q.append((xxx, yyy, lv+1))
        if k > 0:
            for dx, dy in dh:
                xxx, yyy = xx + dx, yy + dy
                # print(123, xxx, yyy)
                if (0 <= xxx < h and 0 <= yyy < w ) and (not board[xxx][yyy] or lv < board[xxx][yyy]+2):
                    q.append((xxx, yyy, lv+1))
            k -= 1
    return lv, False

bfs(0, 0, 1)

if board[h-1][w-1]:
    print(board[h-1][w-1]-1)
else:
    print(-1)
