# Not Completed

from collections import deque
n, m = map(int, input().split())

board = [list(map(int, list(input()))) for _ in range(n)]
# visited = [[0]*m for _ in range(n)]

# print('-'*20, *board, sep='\n')

def copy_board(board):
    return [row[:] for row in board]

def bfs(r, c, board, lv):
    q = deque()
    q.append((r, c, lv))
    candidates = []
    board[r][c] = lv
    # print('-'*20, *board, sep='\n')
    saved = None
    while q:
        rr, cc, next_lv = q.popleft()
        for dr, dc in [(-1, 0), (0, -1), (0, +1), (+1, 0)]:
            rrr, ccc = rr + dr, cc + dc
            if 0<= rrr < n and 0<=ccc<m:
                if not board[rrr][ccc]:
                    board[rrr][ccc] = next_lv + 1
                    if rrr == n-1 and ccc == c-1:
                        return board[rrr][ccc]
                    # print('-'*20, *board, sep='\n')
                    q.append((rrr, ccc, next_lv + 1))
                elif board[rrr][ccc] == 1: # 벽
                    saved = (rrr, ccc)
                    candidates.append((rrr, ccc, next_lv+1))
    return None

cand = bfs(0, 0, board, 2)
if board[n-1][m-1]:
    print(board[n-1][m-1] - 1)
else:
    # print(cand)
    found = False
    for r, c, lv in cand:
        copied_board = copy_board(board)
        copied_board[r][c] = 0
        bfs(r, c, copied_board, lv)
        if copied_board[n-1][m-1]:
            print(copied_board[n-1][m-1] - 1)
            found = True
            break
    if not found:
        print(-1)
