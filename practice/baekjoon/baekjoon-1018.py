N, M = map(int, input().split())
board = [input() for _ in range(N)]
print()
print(*board, sep="\n")

CHESS_WIDTH = CHESS_HEIGHT = 8

B_START = ["BWBWBWBW", "WBWBWBWB"] * 4
W_START = ["WBWBWBWB", "BWBWBWBW"] * 4
min_paint = 64

for i in range(N - CHESS_WIDTH + 1):
    for j in range(M - CHESS_HEIGHT + 1):
        new_board = ""
        print(board[i][j])
        for start in (B_START, W_START):
            diff = 0
            for k, row in enumerate(board[i : i + CHESS_HEIGHT]):
                chess_row = row[j : j + CHESS_WIDTH]
                to_row = start[k]
                print(chess_row, to_row)
                for a, b in zip(chess_row, to_row):
                    if a != b:
                        diff += 1
            print("diff", diff)
            min_paint = min(min_paint, diff)
print(min_paint)
