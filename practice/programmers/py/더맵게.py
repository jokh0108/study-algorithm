from heapq import *


def solution(scoville, K):
    heapify(scoville)
    cnt = 0
    while scoville[0] < K:
        print(scoville)
        if len(scoville) <= 1:
            return -1
        min1 = heappop(scoville)
        min2 = heappop(scoville)
        mix = min1 + 2 * min2
        cnt += 1
        heappush(scoville, mix)
    return cnt


print(solution([12, 42, 23, 19, 510, 12], 13))
print(solution([1, 2, 3, 9, 10, 12], 7))
# print(solution([1]*1000000, 7))
print()
