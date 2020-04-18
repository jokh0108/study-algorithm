from collections import deque, defaultdict
from itertools import combinations

N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]
# print(*sea, sep='\n')

visited = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] = 1 if sea[i][j] == 0 else 0
# print()
# print(*visited, sep='\n')

num = 1
d = [(-1, 0), (0, +1), (+1, 0), (0, -1)]

def bfs(i, j, num):
    data = {}
    q = deque([(i, j)])
    visited[i][j] = 1
    sea[i][j] = num
    while q:
        r, c = q.popleft()
        sea[r][c] = num
        visited[r][c] = 1
        arr = []
        for idx in range(len(d)):
            dr, dc = d[idx]
            rr, cc = r + dr, c + dc
            if 0 <= rr < N and 0 <= cc < M and sea[rr][cc] == 0:
                arr.append(idx)
            if 0 <= rr < N and 0 <= cc < M and not visited[rr][cc]:
                visited[rr][cc] = 1
                q.append((rr, cc))
        if arr:
            data[(r, c, num)] = arr
    # print(d)
    # print(arr)
    # print('sea', *sea, sep='\n')
    # print()
    # print('visited', *visited, sep='\n')
    return data

boundary = {}
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            data = bfs(i, j, num)
            boundary.update(data)
            num += 1
            # print(123, data)

bridges = defaultdict(int)
for c in combinations(range(1, num), 2):
    bridges[c] = 100
# print(*bridges.items(), sep='\n')
# print('sea', *sea, sep='\n')

for (r, c, n), dirs in boundary.items():
    # print(r, c, n, dirs)
    for dir in dirs:
        rr, cc = r, c
        dist = 0
        if dir == 0:
            rr -= 1
            while 0 <= rr and sea[rr][cc] == 0:
                rr -= 1
            if 0<= rr and sea[rr][cc] != 0 and n < sea[rr][cc] and r - rr -1 >= 2:
                bridges[(n, sea[rr][cc])] = min(bridges[(n, sea[rr][cc])], r - rr -1)
                continue
        elif dir == 1:
            cc += 1
            while cc < M and sea[rr][cc] == 0:
                cc += 1
            if cc < M and sea[rr][cc] != 0 and n < sea[rr][cc] and cc - c -1 >= 2:
                bridges[(n, sea[rr][cc])] = min(bridges[(n, sea[rr][cc])], cc - c -1)
                continue
        elif dir == 2:
            rr += 1
            while rr < N and sea[rr][cc] == 0:
                rr += 1
            if rr < N and sea[rr][cc] != 0 and n < sea[rr][cc] and rr - r -1 >= 2:
                bridges[(n, sea[rr][cc])] = min(bridges[(n, sea[rr][cc])], rr - r -1)
        else:
            cc -= 1
            while 0 <= cc and sea[rr][cc] == 0:
                cc -= 1
            if 0 <= cc and sea[rr][cc] != 0 and n < sea[rr][cc] and c - cc - 1 >= 2:
                bridges[(n, sea[rr][cc])] = min(bridges[(n, sea[rr][cc])], c - cc - 1)

# print(*bridges.items(), sep='\n')
to_delete = []
for k, v in bridges.items():
    if v == 100:
        to_delete.append(k)
for x in to_delete:
    del bridges[x]


def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        root[y] = x
    else:
        root[x] = y

if len(bridges) < num - 2:
    print(-1)
else:
    m = 10**12
    for k, v in bridges.items():
        for c in combinations(bridges, num-2):
            # print(c)
            root = [i for i in range(num)]
            for _ in range(2):
                for pair in c:
                    union(*pair)
            f = True
            for r in root[1:]:
                if r != 1:
                    f = False
                    break
            if not f:
                continue
            l = 0
            for pair in c:
                l += bridges[pair]
            if m > l:
                m = l

    if m == 10**12:
        print(-1)
    else:
        print(m)

# if not bridges:
#     print(-1)
# else:
#     m = 10**12
#     for k, v in bridges.items():
#         for c in combinations(bridges, num-2):
#             print(c)
#             component = 1
#             s = set(range(1, num))
#             ss = set()
#             l = 0
#             for pair in c:
#                 print(777, ss & set(pair))
#                 if ss and not (ss & set(pair)):
#                     component += 1
#                 ss.update(set(pair))
#                 l += bridges[pair]
#             print(s, ss, l, component)
#             if component > 1:
#                 continue
#             if s == ss:
#                 if m > l:
#                     m = l
#                     print(s, ss, l)
#     if m == 10**12:
#         print(-1)
#     else:
#         print(m)