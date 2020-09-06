from collections import deque
n = int(input())
answer = 1
area = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
copied_area = [[0] * n for _ in range(n)]
q = deque()
# print(*area, sep='\n')

def copy_area_from(area):
    for i in range(n):
        for j in range(n):
            copied_area[i][j] = area[i][j]

def it_rains_in(area, rain_height, visited):
    for i in range(n):
        for j in range(n):
            if area[i][j] <= rain_height:
                area[i][j] = 0
                visited[i][j] = -1

def bfs(area, visited, area_num, i, j):
    q.clear()
    q.append((i, j))
    visited[i][j] = area_num
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (0, -1), (0, +1), (+1, 0)]:
            rr, cc = r + dr, c + dc
            if 0 <= rr < n and 0 <= cc < n and not visited[rr][cc] and area[rr][cc]:
                visited[rr][cc] = area_num
                q.append((rr, cc))

def init_visited(visited):
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

for rain_height in range(101):
    copy_area_from(area)
    init_visited(visited)
    it_rains_in(copied_area, rain_height, visited)
    # print(rain_height, '-'*20, *copied_area, sep='\n')
    # print('visited', '-'*20, *visited, sep='\n')
    cnt = 1
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(copied_area, visited, cnt, i, j)
                cnt += 1
    # print('visited', '-'*20, *visited, sep='\n')
    if answer < cnt:
        # print(rain_height, 'here', cnt)
        answer = cnt

print(answer-1)
