def solution(A, B):
    answer = 0
    A = sorted(A)
    B = sorted(B)
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            answer += 1
            i += 1
        j += 1
    return answer


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
print(solution([2, 2, 2, 2], [1, 1, 1, 1]))
print(solution([2], [3]))