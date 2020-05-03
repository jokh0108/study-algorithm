def solution(n, s):
    answer = []
    while n >= 1:
        a = s // n
        if a == 0:
            return [-1]
        answer.append(a)
        s = s - a
        n -= 1
    return answer

print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))
