from collections import defaultdict
def diff(w1, w2):
    cnt = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            cnt += 1
    return cnt
def dfs(u, G, visited, level):
    visited[u] = True
    print(u, visited, level)
    for v in G[u]:
        if not visited[v]:
            level[v] = level[u] + 1
            dfs(v, G, visited, level)
    
def solution(begin, target, words):
    if target not in words:
        return 0
    G = defaultdict(list)
    visited = {word : False for word in words}
    level = {word : 0 for word in words}
    # print(visited)
    for i in range(len(words)):
        if diff(begin, words[i]) == 1:
            G[begin].append(words[i])
            G[words[i]].append(begin)
    visited[begin] = False
    level[begin] = 0
    for i in range(len(words)-1):
        for j in range(i+1, len(words)):
            w1 = words[i]
            w2 = words[j]
            if diff(w1, w2) == 1:
                G[w1].append(w2)
                G[w2].append(w1)
    print(G)
    dfs(begin, G, visited, level)
    answer = 0
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))