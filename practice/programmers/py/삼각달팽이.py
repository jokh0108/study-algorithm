dirs = [(1, 0), (0, 1), (-1, -1)]


def solution(n):
    board = [[0] * n for _ in range(n)]
    # print(*board, sep='\n')
    i, j, dir_i = 0, 0, 0
    for k in range(1, n*(n+1)//2 + 1):
        # print(i, j)
        board[i][j] = k
        if i == n-1 and j == 0:
            dir_i = (dir_i + 1) % 3
        elif i == n-1 and j == n-1:
            dir_i = (dir_i + 1) % 3
        else:
            di, dj = dirs[dir_i]
            if board[i+di][j+dj] != 0:
                dir_i = (dir_i + 1) % 3
        di, dj = dirs[dir_i]
        i, j = i+di, j+dj
        # print(*board, sep='\n')
    answer = []
    for row in board:
        filtered = list(filter(lambda x: x != 0, row))
        # print(filtered)
        answer = [*answer, *filtered]
    return answer


# print(solution(4))
# print(solution(5))
# print(solution(6))
