def tobinary(N):
    binary = deque()
    while N != 0:
        binary.appendleft(N % 2)
        N = N // 2
    return binary
    
from collections import deque

N = int(input())
binary = tobinary(N)

hexa = deque()
while N != 0:
    hexa.extendleft(tobinary(N % 10))
    N = N // 10
print(sum(binary), end=' ')
print(sum(hexa))

    