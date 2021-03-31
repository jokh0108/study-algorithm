import collections


def solution(n, edges):
    visited = [False] * (len(edges) + 1)
    graph = collections.defaultdict(list)

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)

    def bfs(v):
        q = collections.deque([(v)])
        visited[v] = True
        d = collections.defaultdict(int)
        d[v] = 1

        while q:
            vv = q.popleft()
            for w in graph[vv]:
                if not visited[w]:
                    q.append(w)
                    visited[w] = True
                    d[w] = d[vv] + 1
        return d
    d = bfs(1)
    # print(d)
    max_distance = max(d.values())
    return len(list(filter(lambda x: x == max_distance, d.values())))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
