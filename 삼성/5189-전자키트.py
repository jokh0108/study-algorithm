import pprint

T = int(input())
for i in range(T):
    board = []
    N = int(input())
    for _ in range(N):
        line = list(map(int, input().split()))
        board.append(line[:])

