import collections


def solution(board):
    answer = 0
    N = len(board)
    rotate_to_vertical = [
        ((0, 0), (-1, -1)),
        ((0, 0), (1, -1)),
        ((-1, 1), (0, 0)),
        ((1, 1), (0, 0)),
    ]
    rotate_to_horizon = [
        ((1, 1), (0, 0)),
        ((1, -1), (0, 0)),
        ((0, 0), (-1, -1)),
        ((0, 0), (-1, 1)),
    ]
    init_position = ((0, 0), (0, 1))
    q = collections.deque([(0, init_position)])
    visited = {init_position: 0}
    print(q, visited)
    while q:
        cur_time, ((x1, y1), (x2, y2)) = q.popleft()
        if x1 - x2 == 0:  # 가로
            for (dx1, dy1), (dx2, dy2) in rotate_to_vertical:
                nx1, ny1, nx2, ny2 = x1 + dx1, y1 + dy1, x2 + dx2, y2 + dy2
                next_position = ((nx1, ny1), (nx2, ny2))
                if (
                    (nx1 < 0 or nx1 > N)
                    or (ny1 < 0 or ny1 > N)
                    or (nx2 < 0 or nx2 > N)
                    or (ny2 < 0 or ny2 > N)
                ):
                    continue
                next_position = sorted(next_position)
                if next_position not in visited:
                    visited[next_position] = cur_time + 1

            pass
        if y1 - y2 == 0:
            # 세로
            pass

    return answer


print(
    solution(
        [
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 1, 1],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0],
        ]
    )
)
