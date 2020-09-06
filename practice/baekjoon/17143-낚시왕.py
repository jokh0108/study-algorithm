def get_closet_shark(sharks, king_pos):
    arr = []
    for shark_num, info in sharks.items():
        if info['c'] == king_pos:
            arr.append((shark_num, sharks[shark_num]["r"]))
    return sorted(arr, key = lambda x: x[1])[0][0]

def move_sharks(sharks):
    for i, info in sharks.items():
        if info['d'] == 1: 
            sharks[i]['r'] -= info['s']
            if sharks[i]['r'] <= 0:
                mod = (sharks[i]['r']-1) % (2 * (R-1))
                if mod >= R-1:
                    sharks[i]['d'] = 2
                    sharks[i]['r'] = (2 * R - 1) - mod
                else:
                    sharks[i]['r'] = mod + 1
        elif info['d'] == 2:
            sharks[i]['r'] += info['s']
            if sharks[i]['r'] > R:
                mod = (sharks[i]['r']-2) % (2 * (R-1))
                if mod >= R-1:
                    sharks[i]['d'] = 1
                    sharks[i]['r'] = 2 * (R - 1) - mod
                else:
                    sharks[i]['r'] = mod + 2
        elif info['d'] == 3: 
            sharks[i]['c'] += info['s']
            if sharks[i]['c'] > C:
                mod = (sharks[i]['c']-2) % (2 * (C-1))
                if mod >= C-1:
                    sharks[i]['d'] = 4
                    sharks[i]['c'] = 2 * (C - 1) - mod
                else:
                    sharks[i]['c'] = mod + 2
        elif info['d'] == 4: 
            sharks[i]['c'] -= info['s']
            if sharks[i]['c'] <= 0:
                mod = (sharks[i]['c']-1) % (2 * (C-1))
                if mod >= C-1:
                    sharks[i]['d'] = 3
                    sharks[i]['c'] = (2 * C - 1) - mod
                else:
                    sharks[i]['c'] = mod + 1

def clear_sharks(sharks):
    pos_info = {}
    to_be_eaten = []
    for i, info in sharks.items():
        r, c = (info['r'], info['c'])
        if pos_info.get((r, c)):
            if pos_info[(r, c)][1] < info['z']:
                to_be_eaten.append(pos_info[(r, c)])[0]
                pos_info[(r, c)] = (i, info['z'])
        else:
            pos_info[(r, c)] = (i, info['z'])
    print(to_be_eaten, pos_info)

def draw_board(board, sharks):
    for i, info in sharks.items():
        r, c = info['r'], info['c']
        board[r][c] = i
    print(*board, sep='\n')
    

R, C, M = map(int, input().split())
board = [[-1 for _ in range(C+1)] for _ in range(R+1)]

print()
print(*board, sep='\n')

sharks = {}
for i in range(M):
    sharks[i] = {}
    r, c, s, d, z = list(map(int, input().split()))
    sharks[i] = {"r": r, "c": c, "s": s, "d": d, "z": z}
    print(i, sharks[i])

total = 0
for king_pos in range(1, C+1):
    shark_num = get_closet_shark(sharks, king_pos)
    total += sharks[shark_num]["z"]
    del sharks[shark_num]
    move_sharks(sharks)
    clear_sharks(sharks)
    draw_board(board[:], sharks)