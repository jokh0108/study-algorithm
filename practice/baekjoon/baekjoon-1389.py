# 케인 베이컨의 6단계 법칙
# bfs?

from collections import deque


def bfs(v, graph):
    count = 0
    visited = [False] * (N + 1)

    q = deque([(v, 0)])
    visited[v] = True

    while q:
        cur, bacon = q.popleft()
        count += bacon
        for neighbor in range(1, N + 1):
            if graph[cur][neighbor] and not visited[neighbor]:
                q.append((neighbor, bacon + 1))
                visited[neighbor] = True
    return count


def solution(N, graph):
    arr = [0] * (N + 1)
    for v in range(1, N + 1):
        arr[v] = bfs(v, graph)
    return arr.index(min(arr[1:]))


N, M = map(int, input().split())
graph = [[False] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

print(solution(N, graph))
