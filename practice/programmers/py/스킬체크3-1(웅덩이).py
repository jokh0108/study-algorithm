

def dfs(i, j, m, n, puddles, visited, step, ans):
    if step == m+n-2:
        ans.append(step)
        print(ans)
        return
    to_left = visited[:]
    print(*visited, sep='\n')
    print(i, j, step)
    if (i+1 <= n) and ([i+1, j] not in puddles):
        if not visited[i+1][j]:
            to_left[i][j] = True
            dfs(i+1, j, m, n, puddles, to_left[:], step+1, ans)
    to_right = visited[:]
    if (j+1 <= m) and ([i, j+1] not in puddles):
        if not visited[i][j+1]:
            to_right[i][j] = True
            dfs(i, j+1, m, n, puddles, to_right[:], step+1, ans)


def solution(m, n, puddles):
    visited = [[False]*(m+1) for _ in range(n+1)]
    print(*visited, sep='\n')
    ans = []
    dfs(1, 1, m, n, puddles, visited[:], 0, ans)
    print(ans)
    return len(ans)


solution(	4, 3, [[2, 2]])
