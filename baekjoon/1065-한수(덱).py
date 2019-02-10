from collections import deque
def isHan(N):
    if N < 100:
        return True
    deq.clear()
    deq.append((N // 100) % 10)
    deq.append((N // 10) % 10)
    deq.append(N % 10)
    while N // 100 != 0 : #세자리수 이상만
        # print(_1, _10, _100)
        #print(deq)
        if deq[0] - deq[1] != deq[1] - deq[2]:
            # print("No")
            return False
        deq.pop()
        N = N // 10
        deq.appendleft((N // 100) % 10)

    # print("Yes")

    return True
deq = deque()
N = int(input())
# isHan(N)
# answer = 0
answer = []
for i in range(1,N+1):
    if isHan(i):
        if i >1000:
            print(i)
        answer.append(i)
print(len(answer))