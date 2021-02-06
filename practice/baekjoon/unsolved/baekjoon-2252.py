# 줄 세우기
from collections import deque


def solution(N, M, comparisons):
    checked = set()
    line_up = deque()
    for a, b in comparisons:
        if a in checked:
            line_up.append(b)
        elif b in checked:
            line_up.appendleft(a)
        else:
            line_up.appendleft(a)
            line_up.append(b)

        checked |= {a, b}
        print(checked)
    unchecked = set(range(1, N + 1)) - checked
    return list(unchecked) + list(line_up)


N, M = map(int, input().split())
comparisons = [list(map(int, input().split())) for _ in range(M)]

print(solution(N, M, comparisons))
