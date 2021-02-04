"""
같은 자릿수 중에서 가장 작은 수 출력
125 -> 100
37 -> 10
3 -> 0
한 자릿수가 특이 케이스
"""

def solution(N):
    if N < 10:
        return 0
    e = 0
    while N:
        e += 1
        N = N // 10
    return pow(10, e-1)

print(solution(125))
print(solution(37))
print(solution(3))
print(solution(10**9))
print(solution(1))
print(solution(10**9-1))

