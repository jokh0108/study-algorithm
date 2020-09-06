# def find_nonzero_minimum(stones):
#     m = 3*(10**9)
#     for i in range(len(stones)):
#         if stones[i] <= 0:
#             continue
#         if m > stones[i]:
#             m = stones[i]
#     return m
#
#
# def solution(stones, k):
#     answer = 0
#     while any(stones):
#         m = find_nonzero_minimum(stones)
#         for i in range(len(stones)):
#             stones[i] -= m
#             if stones[i] < 0:
#                 stones[i] = 0
#         answer += m
#         print(stones)
#         for i in range(len(stones)):
#             print('hello', stones[i + 1: i + 1 + k])
#             if len(stones[i+1: i+1+k]) == k and sum(stones[i+1: i+1+k]) == 0:
#                 return answer
#
#     return answer


def solution(stones, k):
    answer = 0
    stones = sorted([[i, x] for i, x in enumerate(stones)], key=lambda x: (x[1], x[0]))
    print(stones)
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))