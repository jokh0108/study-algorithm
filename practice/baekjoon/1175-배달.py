from collections import deque

GIFT = 2

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
print(board)


def get_start(board, n, m):
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'S':
                return (i, j)


def bfs(start):
    q = deque([start])
    r, c = start
    board[r][c] = 1


start = get_start(board, n, m)
