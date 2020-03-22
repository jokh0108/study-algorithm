import sys
import collections
import copy
import itertools

input = sys.stdin.readline

def get_possibles(r, c, lab, visited):
    dirs = []
    if r-1 >= 0 and not visited[r-1][c] and \
        (lab[r-1][c] == 0 or lab[r-1][c] == 2):
            dirs.append((r-1, c))
    if r+1 < N and not visited[r+1][c] and \
        (lab[r+1][c] == 0 or lab[r+1][c] == 2):
            dirs.append((r+1, c))
    if c-1 >=0 and not visited[r][c-1] and \
        (lab[r][c-1] == 0 or lab[r][c-1] == 2):
            dirs.append((r, c-1))
    if c+1 < N and not visited[r][c+1] and \
        (lab[r][c+1] == 0 or lab[r][c+1] == 2):
            dirs.append((r, c+1))
    return dirs

def bfs(active, lab_copied, disabled):
    time = 2
    d = collections.deque()
    d.extend(active)
    visited = [[False for _ in range(N)] for _ in range(N)]
    for x, y in active:
        visited[x][y] = True
    while d:
        # print(d)
        v = d.popleft()
        possibles = get_possibles(*v, lab_copied, visited)
        # print(v)
        # print("possibles", possibles)
        if not possibles:
            continue
        for r, c in possibles:
            lab_copied[r][c] = lab_copied[v[0]][v[1]] + 1
            visited[r][c] = True
            if (r, c) not in disabled:
                time = max(time, lab_copied[r][c])
            d.append((r, c))
        # print(r, c)    
        # print(*lab_copied, sep='\n')
        # print()

    for row in lab_copied:
        if 0 in row:
            return -1
    # print("time", time)
    return time - 2

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
# print(N, M, *lab, sep='\n')

virus_possible = set()
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus_possible.add((i, j))

# print(virus_possible)


m = 10000000000
answers = []
for active in itertools.combinations(virus_possible, M):
    # print("comb ", active)
    answer = bfs(active, copy.deepcopy(lab), disabled = virus_possible - set(active))
    answers.append(answer)
# print("answers", answers)

if answers.count(-1) == len(answers):
    print(-1)
else:
    print(min([x for x in answers if x != -1]))