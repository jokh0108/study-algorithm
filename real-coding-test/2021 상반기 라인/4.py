N, E, W, S = (-1, 0), (0, 1), (0, -1), (1, 0)
dir_lefthand_map = {
    S: [E, S, W, N],
    E: [N, E, S, W],
    N: [W, N, E, S],
    W: [S, W, N, E],
}

# next_status = {
#     E: 'right',
#     N: 'up',
#     W: 'left',
#     S: 'down',
# }

def solution(maze):
    answer = 0
    n = len(maze)
    status = [S, [0, 0]]
    while status[1] != [n-1, n-1]:
        cur_dir, [y, x] = status
        for lefthand in dir_lefthand_map[cur_dir]:
            dy, dx = lefthand
            ny, nx = y + dy, x + dx
            if 0 <= nx < n and 0 <= ny < n and maze[ny][nx] == 0:
                status = [lefthand, [ny, nx]]
                answer += 1
                print(status)
                break
    return answer

print(solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]))
# print(solution([[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]))
# print(solution(9))
