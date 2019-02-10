from itertools import combinations
from itertools import permutations

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return sieve

def solution(numbers):
    answer =[]
    p = prime_list(9999999+1)
    #print(p)
    l = [x for x in numbers]
    for i in range(len(l)+1):
        for j in combinations(l, i):
            for k in permutations(j):
                temp = "".join(list(k))
                if temp != "":
                    temp = int(temp)
                    if p[temp] == True and (temp not in answer) and temp != 0 and temp != 1:
                        answer.append(temp)
   # print(answer)
    return len(answer)

solution("011")