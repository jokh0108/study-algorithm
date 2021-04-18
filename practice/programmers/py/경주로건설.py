import collections


def solution(board):
    print(*board, sep="\n")
    d = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }
    N = len(board)
    visited = [[False] * N for _ in range(N)]
    print(*visited, sep="\n")

    def bfs():
        q = collections.deque([(0, 0, None, 0)])
        visited[0][0] = True
        while q:
            x, y, cur_direction, cur_cost = q.popleft()
            for next_direction, (dx, dy) in d.items():
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                next_cost = (
                    cur_cost + 100
                    if not cur_direction or cur_direction == next_direction
                    else cur_cost + 600
                )
                print(
                    x, y, cur_cost, cur_direction, nx, ny, next_cost, next_direction, q
                )
                print(not visited[nx][ny] and board[nx][ny] == 0)
                print(visited[nx][ny], board[nx][ny], next_cost)
                if (not visited[nx][ny] and board[nx][ny] == 0) or (
                    visited[nx][ny] and board[nx][ny] >= next_cost
                ):
                    q.append((nx, ny, next_direction, next_cost))
                    board[nx][ny] = next_cost
                    visited[nx][ny] = True
                    print(*board, sep="\n")
            print(q)
            print()

    bfs()
    return board[-1][-1]


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(
    solution(
        [
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
)
