def print_board_info():
    for k, v in board_info.items():
        if v:
            print(k,':', v, end=' || ')
    print()

def get_next_pos(horse):
    x, y, d = horse
    if d == 1: return x, y+1
    if d == 2: return x, y-1
    if d == 3: return x-1, y
    if d == 4: return x+1, y

def get_next_color(next_pos):
    return board_color[next_pos[0]][next_pos[1]]

def pop_upper_horses(horse, idx):
    x, y, _ = horse
    mid = board_info[(x, y)].index(idx)
    lower = board_info[(x, y)][:mid]
    upper = board_info[(x, y)][mid:]
    # print("mid, lower, upper", mid, lower, upper)
    board_info[(x, y)] = lower
    return upper

def update_horses(moving_horse, horse_num, next_pos, next_color):
    upper = []
    if next_color == 0:
        upper = pop_upper_horses(moving_horse, horse_num)
        for horse_num in upper:
            horses[horse_num] = list(next_pos) + [horses[horse_num][2]]
        board_info[next_pos].extend(upper)
    elif next_color == 1:
        upper = pop_upper_horses(moving_horse, horse_num)
        for horse_num in upper:
            horses[horse_num] = list(next_pos) + [horses[horse_num][2]]
        board_info[next_pos].extend(upper[::-1])
    else:
        d = horses[horse_num][2]
        d = (-d + 3) if d < 3 else (-d + 7)
        horses[horse_num][2] = d
        next_next_pos = get_next_pos(horses[horse_num])
        next_next_color = get_next_color(next_next_pos)
        if next_next_color != 2: # if not blue
            update_horses(horses[horse_num], horse_num, next_next_pos, next_next_color)
            next_pos = next_next_pos            
    if len(board_info.get(next_pos, [])) >= 4:
        return True
    return False

N, K = map(int, input().split())

board_color = []
board_color.append([2] * (N+2))
for _ in range(N):
    board_color.append([2] + list(map(int, input().split()))+ [2])
board_color.append([2] * (N+2))

horses = []
for _ in range(K):
    horses.append(list(map(int, input().split())))

# print(*board_color, sep='\n')
# print(*horses, sep='\n')

board_info = {}
for i in range(1, N+1):
    for j in range(1, N+1):
        board_info.update({(i, j) : []})
for idx in range(len(horses)):
    h = horses[idx]
    board_info[(h[0], h[1])].append(idx)

# print_board_info()
# print()

turns = 0
for _ in range(1001):
    turns += 1
    finished = False
    # print('=======================', turns, '=======================')
    for idx in range(len(horses)):
        next_pos = get_next_pos(horses[idx])
        next_color = get_next_color(next_pos)
        # print("cur_horse, cur_pos, dir: ",idx, horses[idx][:2], horses[idx][2])    
        # print("next_pos, next_color: ", next_pos, next_color)    
        finished = update_horses(horses[idx], idx, next_pos, next_color)
        if finished:
            # print('finished')
            break
        # print_board_info()
        # print("--horses--", *horses, sep='\n')
        # print()
    # print()
    if finished:
        break

if turns <= 1000:
    print(turns)
else:
    print(-1)

