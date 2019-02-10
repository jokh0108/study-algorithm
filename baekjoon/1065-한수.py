def isHan(N):
    if N < 100:
        return True
    
    while N // 100 != 0 : #세자리수 이상만
        _1 = N % 10
        _10 = (N // 10) % 10
        _100 = (N // 100) % 10
        # print(_1, _10, _100)
        if _1 - _10 != _10 - _100:
            # print("No")
            return False
        N = N // 10

    # print("Yes")

    return True

N = int(input())
# isHan(N)
# answer = 0
answer = []
for i in range(1,N+1):
    if isHan(i):
        if i >1000:
            print(i)
        answer.append(i)
#print(answer)