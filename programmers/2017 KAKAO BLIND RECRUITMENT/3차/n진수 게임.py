def solution(n, t, m, p):
    # 19:46 ~ 20:12
    hexCode = [str(i) for i in range(10)]+['A','B','C','D','E','F']
    answer = '0'
    for i in range(t * m):
        changed = ''
        num = i
        while num > 0:
            changed = hexCode[num % n] + changed
            num = num // n
        # print(changed)
        answer += changed
    # print(answer)
    return answer[p-1:t*m:m]

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))


