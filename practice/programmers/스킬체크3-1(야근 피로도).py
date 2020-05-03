
import heapq

def print_heap(max_heap):
    h = max_heap[:]
    while h:
        print(heapq.heappop(h)[1], end=' ')
    print()

def solution(n, works):
    max_heap = []
    for work in works:
        heapq.heappush(max_heap, (-work, work))
    while n:
        if max_heap[0][1] == 0:
            break
        new_work = heapq.heappop(max_heap)[1] - 1
        heapq.heappush(max_heap, (-new_work, new_work))
        n -= 1
        # print_heap(max_heap)
    # print(max_heap)

    answer = 0
    for _, x in max_heap:
        answer += x ** 2
    return answer

print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))
# print(solution(10, [1, 5, 4, 6, 5, 4, 8, 3,4, 7, 2, 5, 2]))
