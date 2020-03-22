def getCol(j):
    return [board[i][j] for i in range(100) if board[i][j] >= 1]

def findSticking():
    ans = 0
    for j in range(100):
        col = getCol(j)
        stickON=False
        for each in col:
            if each == 1:
                if not stickON:
                    stickON = True
            else :
                if stickON:
                    ans += 1
                    stickON = False
    return ans

for i in range(1, 11):
    board = [list(map(int, input().split())) for _ in range(int(input()))]
    ans = findSticking()
    # print(board)

    print("#%d"%i, ans)