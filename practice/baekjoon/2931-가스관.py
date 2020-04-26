from collections import deque

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
# print(*board, sep='\n')

d = {
    'N': (-1, 0),
    'E': (0, +1),
    'W': (0, -1),
    'S': (+1, 0)
}

block_dict = {
    '|': {d['N'], d['S']},
    '-': {d['E'], d['W']},
    '+': {d['N'], d['E'], d['W'], d['S']},
    '1': {d['E'], d['S']},
    '2': {d['N'], d['E']},
    '3': {d['N'], d['W']},
    '4': {d['W'], d['S']},
}

for i in range(r):
    for j in range(c):
        if board[i][j] == 'M':
            start = (i, j, 'M')
            break


def my_print(b):
    print('-'*10, *b, '-'*10, sep='\n')


def find_block(rr, cc, rrr, ccc):
    prev = (rr-rrr, cc-ccc)
    s = set([prev])
    for next_ in d:
        # print(123, next_, d[next_], prev)
        if d[next_] == prev:
            continue
        rrrr, cccc = rrr + d[next_][0], ccc + d[next_][1]
        if 0 <= rrrr < r and 0 <= cccc < c:
            next_block = board[rrrr][cccc]
            # print(234, next_block)
            if next_block in block_dict:
                # print(345, next_block, block_dict[next_block])
                if (next_ == 'N' and d['S'] in block_dict[next_block])\
                        or (next_ == 'E' and d['W'] in block_dict[next_block])\
                        or (next_ == 'W' and d['E'] in block_dict[next_block])\
                        or (next_ == 'S' and d['N'] in block_dict[next_block]):
                    s.add(d[next_])
    # print(s)
    for k, v in block_dict.items():
        if v == s:
            return k
    return None


def bfs(v):
    q = deque()
    q.append(v)
    visited = [[0]*c for _ in range(r)]
    while q:
        rr, cc, block = q.popleft()
        if block == 'Z':
            return
        visited[rr][cc] = block
        # my_print(board)
        # my_print(visited)
        if block == 'M':  # M
            for dr, dc in d.values():
                rrr, ccc = rr + dr, cc + dc
                if 0 <= rrr < r and 0 <= ccc < c:
                    if not visited[rrr][ccc] and board[rrr][ccc] not in {'.', 'Z'}:
                        q.append((rrr, ccc, board[rrr][ccc]))
                        break
        else:
            for dr, dc in block_dict[block]:
                rrr, ccc = rr + dr, cc + dc
                if 0 <= rrr < r and 0 <= ccc < c:
                    if not visited[rrr][ccc]:
                        if board[rrr][ccc] == '.':
                            next_block = find_block(rr, cc, rrr, ccc)
                            return (rrr+1, ccc+1, next_block)
                        q.append((rrr, ccc, board[rrr][ccc]))
                        break


print(*bfs(start), end=' ')
