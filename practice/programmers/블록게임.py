def is_block(block, garo=True):
    if garo:
        block_num = block[1][0]
        if block[1] != [block_num]*3:
            return False
        if not block_num:
            return False
        if block[0] == [block_num, 0, 0]:
            return True
        if block[0] == [0, block_num, 0]:
            return True
        if block[0] == [0, 0, block_num]:
            return True
    else:
        block_num = block[2][0]
        if block[2] != [block_num]*2:
            return False
        if not block_num:
            return False
        if block[0] == [block_num, 0] and block[1] == [block_num, 0]:
            return True
        if block[0] == [0, block_num] and block[1] == [0, block_num]:
            return True
    return False


def are_blocks_above(i, j, board, garo=True):
    if garo:
        s = {j, j + 1, j + 2}
        if board[i][j] != 0:
            s.remove(j)
        elif board[i][j+1] != 0:
            s.remove(j+1)
        elif board[i][j+2] != 0:
            s.remove(j+2)
        a, b = s.pop(), s.pop()
        for r in range(i):
            if board[r][a] != 0:
                return False
            if board[r][b] != 0:
                return False
    else:
        s = {j, j + 1}
        if board[i][j] != 0:
            s.remove(j)
        elif board[i][j+1] != 0:
            s.remove(j+1)
        a = s.pop()
        for r in range(i):
            if board[r][a] != 0:
                return False
    return True


def erase(i, j, board, garo):
    if garo:
        board[i][j] = board[i][j+1] = board[i][j+2] = 0
        board[i+1][j] = board[i+1][j+1] = board[i+1][j+2] = 0
    else:
        board[i][j] = board[i][j+1] = 0
        board[i+1][j] = board[i+1][j+1] = 0
        board[i+2][j] = board[i+2][j+1] = 0


def solution(board):
    print(*board, sep='\n')
    answer = 0
    n = len(board)
    while True:
        cnt = 0
        for i in range(n):
            for j in range(n):
                if j + 2 < n and i + 1 < n:
                    garo = [
                        board[i][j:j + 3],
                        board[i + 1][j:j + 3],
                    ]
                    if is_block(garo, True):
                        if are_blocks_above(i, j, board, True):
                            cnt += 1
                            erase(i, j, board, True)
                            continue
                if j+1 < n and i+2 < n:
                    sero = [
                        board[i][j:j + 2],
                        board[i + 1][j:j + 2],
                        board[i + 2][j:j + 2],
                    ]
                    if is_block(sero, False):
                        if are_blocks_above(i, j, board, False):
                            cnt += 1
                            erase(i, j, board, False)
        if not cnt:
            break
        answer += cnt
    return answer

print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))