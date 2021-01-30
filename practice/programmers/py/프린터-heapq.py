import heapq

def solution(priorities, location):
    priorities = [(-v, v, i) for i, v in enumerate(priorities)]
    heapq.heapify(priorities)
    cnt = 0
    while priorities:
        cnt += 1
        a, v, i = heapq.heappop(priorities)
        print(a, v, i)
        if i == location:
            return cnt

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
