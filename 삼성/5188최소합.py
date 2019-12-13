T = int(input())
for i in range(T):
    board = []
    N = int(input())
    for _ in range(N):
        board.append(map(int, input().split()))
    print(board)