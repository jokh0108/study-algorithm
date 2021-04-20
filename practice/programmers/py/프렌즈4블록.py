def solution(m, n, board):
    def is_four_block(row, col):
        return (
            board[row][col]
            == board[row + 1][col]
            == board[row][col + 1]
            == board[row + 1][col + 1]
            != 0
        )

    def block_down():
        for col in range(n):
            arr = [board[row][col] for row in range(m)]
            arr = list(filter(lambda x: x != 0, arr))
            arr = [0] * (m - len(arr)) + arr
            for row in range(m):
                board[row][col] = arr[row]

    board = [list(row) for row in board]
    count = 0
    while True:
        to_remove = set()
        for row in range(m - 1):
            for col in range(n - 1):
                if is_four_block(row, col):
                    to_remove.add((row, col))
                    to_remove.add((row + 1, col))
                    to_remove.add((row, col + 1))
                    to_remove.add((row + 1, col + 1))
        if not to_remove:
            return count
        count += len(to_remove)
        for row, col in to_remove:
            board[row][col] = 0
        block_down()


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
