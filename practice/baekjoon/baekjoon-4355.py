from collections import defaultdict

# 오일러 파이 함수
# https://nuriwiki.net/wiki/%EC%98%A4%EC%9D%BC%EB%9F%AC_%ED%94%BC_%ED%95%A8%EC%88%98

def getPrimeFactor(n):
    PrimeFactor = defaultdict(lambda: 0)

    # for factor in range(2, int(n**0.5)):
    for factor in range(2, n + 1):
        while n % factor == 0:
            PrimeFactor[factor] += 1
            n = n // factor
        if n == 1:
            break
    return PrimeFactor


while True:
    n = int(input())
    if n == 0:
        break

    primeFactor = getPrimeFactor(n)
    # print(primeFactor)
    # for each in nd:
    #     if each in pl:
    #         primeFactor.append(each)
    result = 1
    for each in primeFactor.items():
        result *= each[0]**each[1]-each[0]**(each[1]-1)
    print(result)
    # for i in range(1, n):
    #     bd = getDivisor(i)
    #     for each in bd:
    #         if each in nd:
    #             Coprime += 1
    #             break
    # print(n - 1 - Coprime)
