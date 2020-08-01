R, C, T = map(int, input().split())

house = [list(map(int, input().split())) for _ in range(R)]
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

def spread_from():
    global house
    delta = [[0]*C for i in range(R)]
    for r in range(R):
        for c in range(C):
            if house[r][c] >= 5:
                d = house[r][c] // 5
                for dr, dc in (-1, 0), (0, -1), (0, 1), (1, 0):
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < R and 0 <= cc < C and house[rr][cc] >= 0 :
                        delta[rr][cc] += d
                        house[r][c] -= d
    # print(*delta, sep='\n')
    for r in range(R):
        for c in range(C):
            house[r][c] += delta[r][c]            

def clean(path):
    for i in range(1, len(path)):
        r, c = path[i]
        rr, cc = path[i-1]
        house[rr][cc] = house[r][c]
    house[path[-1][0]][path[-1][1]] = 0
     
# def print_house():
    # print('==========house==========')
    # for r in range(R):
    #     for c in range(C):
    #         print("%3d "%(house[r][c]), end='')
    #     print()

for r in range(R):
    if house[r][0] == -1:
        r1 = r
        r2 = r1 + 1
        break

upper_path = [(r1, c) for c in range(1, C)] +\
             [(r, C-1) for r in range(r1-1, -1, -1)]+\
             [(0, c) for c in range(C-2, -1, -1)]+\
             [(r, 0) for r in range(1, r1)]

upper_path.reverse()

# print(upper_path)
 
lower_path = [(r2, c) for c in range(1, C)] +\
             [(r, C-1) for r in range(r2+1, R)]+\
             [(R-1, c) for c in range(C-2, -1, -1)]+\
             [(r, 0) for r in range(R-2, r2, -1)]

lower_path.reverse()
# print(lower_path)

for _ in range(T):
    spread_from()
    # print_house()   

    clean(upper_path)
    clean(lower_path)
    # print_house()

print(sum(map(sum, house))+2)