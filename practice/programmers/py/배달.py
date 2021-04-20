import collections


def solution(N, roads, K):
    answer = 0
    times = [0] * (N + 1)
    visited = [False] * (N + 1)
    graph = collections.defaultdict(list)
    for a, b, cost in roads:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    print(graph)

    def bfs(start):
        times[start] = 0
        visited[start] = True
        q = collections.deque([(start, 0)])
        while q:
            v, time = q.popleft()
            for neighbor, cost in graph[v]:
                if not visited[neighbor]:
                    times[neighbor] = time + cost
                    q.append((neighbor, times[neighbor]))
                    visited[neighbor] = True
                    continue
                if visited[neighbor] and time + cost < times[neighbor]:
                    times[neighbor] = time + cost
                    q.append((neighbor, times[neighbor]))

    bfs(1)
    return len(list(filter(lambda x: x <= K, times[1:])))


print(
    solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3)
)
