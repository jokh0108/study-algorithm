# 줄 세우기
from collections import deque


def topological_sort(graph, degrees):
    q = deque([i for i, v in enumerate(degrees) if v == 0 and i != 0])
    result = []
    for _ in range(1, N + 1):
        if not q:
            print("cycle")
            return
        x = q.popleft()
        result.append(str(x))
        for v in graph[x]:
            degrees[v] -= 1
            if degrees[v] == 0:
                q.append(v)
    return " ".join(result)


def solution(N, M, comparisons):
    graph = [[] for _ in range(N + 1)]
    degrees = [0] * (N + 1)

    for a, b in comparisons:
        graph[a].append(b)
        degrees[b] += 1

    return topological_sort(graph, degrees)


N, M = map(int, input().split())
comparisons = [list(map(int, input().split())) for _ in range(M)]

print(solution(N, M, comparisons))
