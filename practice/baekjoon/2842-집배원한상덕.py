from collections import deque

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1 , -1, 1, -1, 0, 1]
answer = 10**10
n = int(input())
board = [input() for _ in range(n)]
house_num = 0
print(board)
for i in range(n):
  for j in range(n):
    if board[i][j] == 'K':
      house_num += 1
    elif board[i][j] == 'P':
      post_pos = (i, j)

height = [list(map(int, input().split())) for _ in range(n)]
print(height)
print(house_num, post_pos)

flatten_height = []
for row in height:
    flatten_height.extend(row)
flatten_height = sorted(list(set(flatten_height)))
print(flatten_height)

start, end = 0, len(flatten_height)-1

def print_visited(visited):
    print('-'*10, *visited, '-'*10, sep='\n')

def bfs(v):
    x, y = v
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = height[x][y]
    print_visited(visited)
    q = deque()
    q.append(v)
    cnt = 0
    while q:
        xx, yy = q.popleft()
        for i in range(8):
            xxx, yyy = xx + dx[i], yy + dy[i]
            if 0 <= xxx < n and 0 <= yyy < n and not visited[xxx][yyy]:
                if flatten_height[start] <= height[xxx][yyy] <= flatten_height[end]:
                    visited[xxx][yyy] = height[xxx][yyy]
                    q.append((xxx, yyy))
                    print_visited(visited)
                    if board[xxx][yyy] == 'K':
                        cnt += 1
    print(cnt, house_num, 'z'*10)
    return cnt == house_num

while start <= end:
    print('new start !!!!!!!!!!!!!!!!!!')
    possible = bfs(post_pos)
    if possible:
        print('possible!!!!!!!!!!!!!!!!!')
        start += 1
        if answer > flatten_height[end] - flatten_height[start]:
            answer = flatten_height[end] - flatten_height[start]
        print(answer)
    else:
        print('impossible!!!!!!!!!!!!!')
        end -= 1

print(answer)
