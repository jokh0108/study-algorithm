from collections import deque

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1 , -1, 1, -1, 0, 1]

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
    print('-'*10, *visited, '-'*10, end='\n')

def bfs(v):
    x, y = v
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = height[x][y]
    print(visited)
    q = deque()
    q.append(v)
    while q:
        xx, yy = q.popleft()
        for i in range(8):
            xxx, yyy = xx + dx[i], yy + dy[i]
            if 0 <= xxx < n and 0 <= yyy < n and not visited[xxx][yyy]:
                visited[xxx][yyy] = height[xxx][yyy]
                q.append((xxx, yyy))
                print_visited(visited)
            print(xxx, yyy)


bfs(post_pos)
