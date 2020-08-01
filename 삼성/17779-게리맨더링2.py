N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

N = 20
board = [[5 for _ in range(N)] for _ in range(N)]

# print(*board, sep='\n')
total = sum([sum(r) for r in board])
# print(total)


def get_area_co(section, x, y, d1, d2, temp_board):
    area = []
    if section == 1:
        for r in range(x+d1-1):
            for c in range(y):
                area.append((r, c))
    elif section == 2:
        for r in range(x+d2):
            for c in range(y, N):  
                area.append((r, c))
                if temp_board[r][c-1] == 0 and temp_board[r][c] == 5:
                    for _ in range(c-y+1):
                        area.pop()
    elif section == 3:
        for r in range(x+d1-1, N):
            for c in range(y-d1+d2-1):
                if temp_board[r][c] == 5 and temp_board[r][c+1] != 5:
                    break
                area.append((r, c))
    elif section == 4:
        for r in range(x+d2, N):
            for c in range(y-d1+d2-1, N):
                area.append((r, c))
    return area

def mark(x, y, d1, d2):
    
    def mark5():
        temp = []
        for i in range(d1+1):
            temp.append((x+i-1, y-i-1))
            # if i == 0:
            #     continue
            # left.append((x+i-1, y-i-1))
        for i in range(d2+1):
            temp.append((x+i-1, y+i-1))
        for i in range(d2+1):
            temp.append((x+d1+i-1, y-d1+i-1))
            # if i == d2:
            #     continue
            # left.append((x+d1+i-1, y-d1+i-1))
        for i in range(d1+1):
            temp.append((x+d2+i-1, y+d2-i-1))
        for r, c in temp:
            temp_board[r][c] = 5
        for r in range(x, x+d1+d2-1):
            # left_bound = left.pop()
            # c = left_bound[1]
            c = 0
            for i in range(N):
                if temp_board[r][i] == 5:
                    c = i
                    break
            for i in range(c+1, N):
                if temp_board[r][i] == 5:
                    break
                else:
                    temp_board[r][i] = 5

    # print(x, y, d1, d2)
    sums = {i+1: 0 for i in range(5)}
    temp_board = [[0]*N for _ in range(N)]
    mark5()
    # print(*temp_board, sep='\n')
    for i in range(1, 5):
        area = get_area_co(i, x, y, d1, d2, temp_board)
        for r, c in area:
            if temp_board[r][c] != 5:
                temp_board[r][c] = i
                sums[i] += board[r][c]
        # print(*temp_board, sep='\n')
    sums[5] = total - sum(list(sums.values()))
    print(sums, total)
    if sums[5] < 0:
        print(*board, sep='\n')
        # print(*temp_board, sep='\n')
    print(*temp_board, sep='\n')
    return max(sums.values()) - min(sums.values())

m = 100*20*20+1
for d1 in range(1, N):
    for d2 in range(1, N):
        for x in range(1, N):
            for y in range(N):
                if x+d1+d2 <= N and 1 <= y-d1 and y+d2 <= N:
                    print(x, y, d1, d2)
                    diff = mark(x, y, d1, d2)
                    # print(m, diff)
                    m = min(diff, m)
print(m)