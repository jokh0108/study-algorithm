# 채점 결과
# 정확성: 50.0
# 효율성: 41.5
# 합계: 91.5 / 100.0

# 효율성 2개 틀렸는데 뭔가 언어적 이슈같다.

import collections


def solution(n, path, order):
    graph = collections.defaultdict(list)
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    before_of = {
        # after: before
        b: a
        for a, b in order
    }
    print(before_of)
    print(graph)
    q = collections.deque([0])
    before_set = set()
    visited = set([0])
    answer = []
    while q:
        after = q.popleft()
        if after in before_of:
            before_set.remove(before_of[after])
            if before_of[after] not in visited:
                # if after in q:
                #     return False
                q.append(after)
                before_set.add(before_of[after])
                if len(before_set) == len(q) and not before_set & visited:
                    print(666, before_set)
                    return False
                print(222, visited, q, before_set)
                continue
        for w in graph[after]:
            if w not in visited:
                q.append(w)
                if w in before_of:
                    before_set.add(before_of[w])
        visited.add(after)
        answer.append(after)
        print(333, visited, q, before_set)
    print(visited)
    print(answer)

    return True


print(
    solution(
        9,
        [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]],
        [[8, 5], [6, 7], [4, 1]],
    )
)

print(
    solution(
        9,
        [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]],
        [[4, 1], [8, 7], [6, 5]],
    )
)
