dirs = "ENWS"

d = {
    "N": (0, +1),
    "W": (-1, 0),
    "E": (+1, 0),
    "S": (0, -1)
}

a, b = map(int, input().split())
n, m = map(int, input().split())

board = [[0] * a for _ in range(b)]

# print(*board, sep='\n')
robots = {}

for i in range(n):
    x, y, z = input().split()
    x, y = int(x)-1, int(y)-1
    board[y][x] = z
    robots[i+1] = [x, y, z]

def find_robot_num_by_pos(robots, x, y):
    for k, v in robots.items():
        xx, yy, _ = v
        if xx == x and yy == y:
            return k

# print(*board, sep='\n')

result = 'OK'

for _ in range(m):
    num, order, it = input().split()
    num, it = map(int, (num, it))
    if order == 'L' or order == 'R':
        x, y, z = robots[num]
        idx = dirs.index(z)
        idx = idx + it if order =='L' else idx - it
        idx = idx % len(dirs)
        robots[num][2] = dirs[idx]
        board[y][x] = dirs[idx]
        # print('-'*20, *board, sep='\n')
    else: # order == 'F'
        _, _, z = robots[num]
        dx, dy = d[z]
        for _ in range(it):
            x, y, _ = robots[num]
            prev_x, prev_y = x, y
            new_x, new_y = x + dx, y + dy
            if not (0 <= new_x < a and 0 <= new_y < b):
                result = f'Robot {num} crashes into the wall'
                break
            if board[new_y][new_x] != 0:
                crashed_robot = find_robot_num_by_pos(robots, new_x, new_y)
                result = f'Robot {num} crashes into robot {crashed_robot}'
                break
            board[new_y][new_x] = z
            board[prev_y][prev_x] = 0
            robots[num] = [new_x, new_y, z]
            # print('-'*20, *board, sep='\n')
        if result != 'OK':
            break

print(result)
