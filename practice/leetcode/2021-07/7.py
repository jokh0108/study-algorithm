import collections
import heapq


def solution(arr):
    half = len(arr) // 2
    arr = [(-v, v, k) for k, v in collections.Counter(arr).items()]
    print(arr)
    heapq.heapify(arr)
    count = 0
    removed_set = set()
    while count < half:
        _, value, key = heapq.heappop(arr)
        print(value, key)
        removed_set.add(key)
        count += value
    print(removed_set)
    return len(removed_set)


# print(solution([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
# print(solution([7, 7, 7, 7, 7, 7]))
# print(solution([1, 9]))
# print(solution([1000, 1000, 3, 7]))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([9, 77, 63, 22, 92, 9, 14, 54, 8, 38, 18, 19, 38, 68, 58, 19]))
