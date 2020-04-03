from collections import Counter

def solution(arr):
    c = Counter(arr)
    M = 0
    M_key = 0
    for k, v in c.items():
        if M < v and k == v:
            M = v
            M_key = k
    return M_key


print(solution([3, 8, 3, 2, 2, 3]))
print(solution([7, 1, 2, 8, 2]))
print(solution([3, 1, 4, 1, 5]))
print(solution([5, 5, 5, 5, 5]))