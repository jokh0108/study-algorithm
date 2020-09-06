from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# def bprint(board):
    # print('-'*20, *board, sep='\n')


def bfs(start, board):
    global OUTER_AIR
    d = {}
    q = deque([start])
    board[start[0]][start[1]] = OUTER_AIR
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (0, -1), (0, +1), (+1, 0)]:
            rr, cc = r + dr, c + dc
            if 0 <= rr < n and 0 <= cc < m:
                if board[rr][cc] == 0:
                    q.append((rr, cc))
                    board[rr][cc] = OUTER_AIR
                elif board[rr][cc] == 1:
                    if not d.get((rr, cc)):
                        d[(rr, cc)] = 1
                    else:
                        d[(rr, cc)] += 1
    # print(d)
    # bprint(board)
    to_be_melted = []
    for k, v in d.items():
        if v >= 2:
            to_be_melted.append(k)
    return to_be_melted


def copy_board(board):
    return [row[:] for row in board]


def melt_cheeze(targets, board):
    for r, c in targets:
        board[r][c] = 0

OUTER_AIR = 2
start = (0, 0)
time = 0
while True:
    to_be_melted = bfs(start, copy_board(board))
    if to_be_melted:
        melt_cheeze(to_be_melted, board)
        # bprint(board)
    else:
        break
    time += 1
print(time)
