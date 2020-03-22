# BFS, 백트래킹
from collections import deque


n = int(input())
arr = list(map(int, input().split()))
deq = deque()
deq.append(arr[0])

# bfs로 풀었지만 
# 0,0,0,0,0,0,0, ... 이런 예제라면 2^n승으로 터질 수 있다.
# 메모이제이션으로 극복! d[i][j] = i번째 단계에서 숫자 j가 나타난 횟수 (처음 숫자가 0번째 단계)
# O(n)으로 끝낼 수 있다.
d = [[0]*21 for _ in range(n-1)]
d[0][arr[0]] = 1
for i in range(1, len(arr)-1):
    length = len(deq)
    print(*d, sep='\n')
    print(len(deq), deq)
    for j in range(length):

        new = deq[j] + arr[i]
        if 0<=new<=20:
            if not d[i][new]:
                deq.append(deq[j] + arr[i])
            d[i][new] += d[i-1][deq[j]]
            

        new = deq[j] - arr[i]
        if 0<=new<=20:
            if not d[i][new]:
                deq.append(deq[j] - arr[i])
            d[i][new] += d[i-1][deq[j]]
            
    for _ in range(length):
        deq.popleft()
print(*d, sep='\n')
print(len(deq), deq)
print(d[n-2][arr[-1]])
