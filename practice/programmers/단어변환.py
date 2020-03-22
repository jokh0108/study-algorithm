m = 9999999
lst = []

def dfs(visited, adj_list, target, v, cnt):
    global m
    lst.append(v)
    # print(lst, cnt)
    if target == v:
        # print(cnt)
        if m > cnt:
            # print(cnt)
            m = cnt
        return 0
    visited[v] = True
    # print(v, end=' ')
    for other in adj_list[v]:
        if not visited[other]:
            dfs(visited, adj_list, target, other, cnt+1)
            lst.pop()
            # print(lst, cnt)


def onlyOneDiff(one, other):
    cnt = 0
    for i in range(len(one)):
        if one[i] != other[i]:
            cnt +=1
    if cnt == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    global m
    if target not in words:
        return 0

    # initialization
    adj_list = {word: [] for word in words}
    adj_list[begin] = []
    visited = {word : False for word in words}
    visited[begin] = True

    for word in words:
        if onlyOneDiff(begin, word):
            adj_list[begin].append(word)
    for word in words:
        for i in range(len(words)):
            if word != words[i]:
                if onlyOneDiff(word, words[i]):
                    adj_list[word].append(words[i])
    # for e in adj_list.items()
#     #     #     print(e):
    dfs(visited, adj_list, target, begin, cnt=0)

    return m


# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print()
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))

