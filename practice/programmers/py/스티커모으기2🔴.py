import collections


def solution(stickers):
    answer = 0
    visited = collections.defaultdict(int)
    n = len(stickers)
    q = collections.deque([(0, tuple(range(n)))])
    print(q)
    while q:
        accumulator, cur_indicies = q.popleft()
        for i in cur_indicies:
            new_accumulator = accumulator + stickers[i]
            new_indices = tuple(
                j if j not in ((i - 1) % n, i, (i + 1) % n) else -1
                for j in cur_indicies
            )
            new_indices = tuple(filter(lambda x: x != -1, new_indices))
            print(cur_indicies, new_indices)
            if (new_indices not in visited) or (
                new_indices in visited and visited[new_indices] < new_accumulator
            ):
                visited[new_indices] = new_accumulator
                q.append((new_accumulator, new_indices))
    print(visited)

    return max(visited.values())


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
# print(solution([1, 3, 2, 5, 4]))
# print(solution([5, 4, 2, 5, 4]))
