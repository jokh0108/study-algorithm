# Not Completed

from collections import deque

def fire_bfs(fires, board):
    q = deque()
    q.append(sangun)
    r, c, start = sangun
    board[r][c] = start
    while q:
        rr, cc, lv = q.popleft()
        lv = int(lv)
        for dr, dc in [(-1, 0), (0, -1), (0, +1), (+1, 0)]:
            rrr, ccc = rr + dr, cc + dc
            if 0 <= rrr < h and 0 <= ccc < w:
                if board[rrr][ccc] == '.':
                    q.append((rrr, ccc, str(lv+1)))
                    board[rrr][ccc] = str(lv+1)
            else:
                return True
    return False


def sangun_bfs(sangun, board):
    q = deque()
    q.append(sangun)
    r, c, start = sangun
    board[r][c] = start
    while q:
        rr, cc, lv = q.popleft()
        lv = int(lv)
        for dr, dc in [(-1, 0), (0, -1), (0, +1), (+1, 0)]:
            rrr, ccc = rr + dr, cc + dc
            if 0 <= rrr < h and 0 <= ccc < w:
                if board[rrr][ccc] == '.':
                    q.append((rrr, ccc, str(lv+1)))
                    board[rrr][ccc] = str(lv+1)
            else:
                return True
    return False

def copy_board(board):
    return [row[:] for row in board]

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):

            print(f'{board[i][j]:1}', end=' ')
        print()

def solve(w, h, board):
    fires, sangun = [], None
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                fires.append((i, j, 0))
            elif board[i][j] == '@':
                sangun = (i, j, 0)
    print(fires, sangun)
    fire_board = copy_board(board)
    sangun_board = copy_board(board)

    # fire_bfs(fires, fire_board)
    sangun_bfs(sangun, sangun_board)
    print_board(sangun_board)

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    print(*board, sep='\n')
    solve(w, h, board)
