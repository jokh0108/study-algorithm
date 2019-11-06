import pprint

T = int(input())
for i in range(T):
    board = []
    N = int(input())
    for _ in range(N):
        line = list(map(int, input().split()))
        board.append(line[:])
    # pprint.pprint(board)

    for j in range(1, N):
        board[0][j] += board[0][j-1]
        board[j][0] += board[j-1][0]

    for j in range(1, N):
        for k in range(1, N):
            board[j][k] += min(board[j-1][k], board[j][k-1])
            # pprint.pprint(board)
    print("#%d"%(i+1), board[N-1][N-1])


