def dfs(visited, n, computers, v):
    # print(v, end ='')
    visited[v] = True
    for i in range(n):
        if computers[v][i] == 1 and not visited[i]:
            dfs(visited, n, computers, i)


def solution(n, computers):
    answer = 0
    visited=[False]*n
    for i in range(n):
        if not visited[i]:
            dfs(visited, n, computers, i)
            # print()
            answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print()
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
