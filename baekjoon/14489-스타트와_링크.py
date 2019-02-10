from itertools import combinations
N = int(input())
board = []
for i in range(N):
    row = [int(x) for x in input().split()]
    board.append(row)
for i in range(N):
    for j in range(N):
        if j > i:
            board[i][j] = board[i][j] + board[j][i]
            board[j][i] = 0
cnt = 0
minimum = 40000
for each in combinations(range(1, N),N//2-1):
    start = set([0])
    start = start.union(each)
    link = set(range(N)).difference(start)
    #print(start, link)
    startStat = 0
    linkStat = 0
    for pair in combinations(list(start), 2):
        #print(pair)
        startStat += board[pair[0]][pair[1]]
    for pair in combinations(list(link), 2):
        #print(pair)
        linkStat += board[pair[0]][pair[1]]
    diff = abs(startStat-linkStat)
    if diff == 0 :
        minimum = diff
        #print(diff)
        break
    if minimum > diff:
        minimum = diff
print(minimum)