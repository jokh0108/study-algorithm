from collections import deque


def bfs(root, dist):
    global M
    dist[root] = 0
    q = deque()
    q.append(root)

    while q:
        v = q.popleft()
        next = [v+1, v-1, v*2, v-10]
        for w in next:
            if w == M:
                return dist[v] + 1
            if 1 <= w <= 10**6 and dist[w] == -1:
                # dist[w] == -1 means that w is visited not yet
                dist[w] = dist[v] + 1
                q.append(w)


T = int(input())
for t in range(T):
    ans = 0
    N, M = map(int, input().split())
    d = [-1] * (10**6 + 1)
    ans = bfs(N, d)

    print("#%d" % (t+1), ans)
