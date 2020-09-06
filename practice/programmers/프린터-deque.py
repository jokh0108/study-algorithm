from collections import deque

def solution(priorities, location):
    q = deque([(v, i) for i, v in enumerate(priorities)])
    d = {}
    cnt = 0
    while q:
        cnt += 1
        v, i = q.popleft()
        for left in q:
            if v < left[0]:
                cnt -=1
                q.append((v, i))
                break
        d[i] = cnt
    return d[location]

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
