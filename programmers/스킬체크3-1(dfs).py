from collections import deque

M = 0

def dfs(v, G, visited, lv):
    visited[v] = True
    print(v, lv)
    
    for u in G[v]:
        if not visited[u]:
            lv[u] = lv[v] + 1
            dfs(u, G, visited, lv)   

def solution(n, edge):
    visited = [False for _ in range(n+1)]
    G = [[] for _ in range(n+1)]
    lv = [0 for _ in range(n+1)]

    for i in range(len(edge)):
        u, v = edge[i]
        G[u].append(v) 
        G[v].append(u) 
        print(G)
    dfs(1, G, visited, lv)
    # return answer
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))