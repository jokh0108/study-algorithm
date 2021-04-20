import collections


def solution(n, weaks, dists):
    def filter_weaks(a, b, weaks) -> tuple:
        if a < 0:
            new_weaks = set(filter(lambda x: b < x < n + a, weaks))
        elif b >= n:
            new_weaks = set(filter(lambda x: b - n < x < a, weaks))
        else:
            new_weaks = set(filter(lambda x: 0 <= x < a or b < x < n, weaks))
        return tuple(sorted(new_weaks))

    dists = sorted(dists)[::-1]
    q = collections.deque([(0, tuple(weaks))])
    weak_set = set()
    while q:
        index, cur_weaks = q.popleft()
        if index == len(dists):
            return -1
        dist = dists[index]
        for weak in cur_weaks:
            # [counter, clockwise]
            for a, b in [(weak - dist, weak), (weak, weak + dist)]:
                remained_weaks = filter_weaks(a, b, cur_weaks)
                if not remained_weaks:
                    return index + 1
                if remained_weaks not in weak_set:
                    weak_set.add(remained_weaks)
                    q.append((index + 1, remained_weaks))
        print("next dist", q)
    return len(dists)


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
