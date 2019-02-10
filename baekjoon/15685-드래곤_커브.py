# 원점 이동 -> 회전 -> 원점 이동(행렬)
def move(p, x, y):    
    return [p[0]-x, p[1]-y]

def rotate(p):
    return [-p[1], p[0]]

def next_curve(L, end):
    #이동
    for i in range(len(L)-2, -1, -1):
        new = L[i]
        new = move(new, end[0], end[1])
        new = rotate(new)
        new = move(new, -end[0], -end[1])
        if 0 <= new[0] <= 100 and 0<= new[1] <= 100:
            L.append(new)
    return L[-1]

def checkBoard(board):
    ans = 0
    for i in range(100):
        for j in range(100):
            if board[i][j] == board[i+1][j+1] == board[i][j+1] == board[i+1][j] == 1:
                ans +=1

    return ans

# 100 X 100 행렬 만든 다음 0/1

# 다 돌고 난 후에 정사각형 체크(print)

board = []
for _ in range(101):
    board.append([0]*101)
# for i in range(100):
#     print(board[i])

N = int(input())
for i in range(N):
    x, y, d, g = [int(x) for x in input().split()]
    start = [x, y]
    if d == 0 : x += 1
    elif d == 1: y -= 1
    elif d == 2: x -= 1
    elif d == 3: y += 1
    end = [x, y]
    # print(start, end)
    point_list = [start, end]
    for j in range(g):
        end = next_curve(point_list, end)
    for each in point_list:
        if 0 <= each[0] <= 100 and 0<= each[1] <= 100:
            board[each[0]][each[1]] = 1
    # for j in range(100):
    #     for k in range(100):
    #         print(board[k][j],end='')
    #     print()
print(checkBoard(board))
