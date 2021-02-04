# from collections import deque
# right_most = 200000
# visited = [False] * (right_most + 1)
# C, B = map(int, input().split())
# timing = {}

# if C == B:
#     print(0)
#     exit()

# q = deque([B])
# sec = 1
# C = C + 1
# while C <= right_most: 
#     print(C)
#     n = q.popleft()
#     if not visited[n]:
#         visited[n] = True
#         if n - 1 >= 0:
#             print(n-1, end=' ')
#             if n - 1 == C:
#                 print(sec)
#                 break
#             q.append(n-1)
#         if n + 1 <= right_most:
#             print(n+1, end=' ')
#             if n + 1 == C:
#                 print(sec)
#                 break
#             q.append(n+1)
#         if n * 2 <= right_most:
#             print(n*1, end=' ')
#             if n * 2 == C:
#                 print(sec)
#                 break
#             q.append(n*2)
#     print()
#     sec += 1
#     C = C + sec

from collections import deque
C, B = map(int,input().split())
right_most = 200000
cony = [C]
brown = [0]*(right_most + 1)
brown[B] = True

for i in range(1,1000):
    if cony[i-1] >= right_most:
        break
    cony.append(cony[i-1]+i)

deq = deque()
deq.append(B)
brown[B] = 0
while deq:
    n = deq.popleft()
    if n-1 >= 0 and brown[n-1] == 0:
        brown[n-1] = brown[n] + 1
        deq.append(n-1)

    if n+1 <= right_most and brown[n+1] == 0:  
        brown[n+1] = brown[n] + 1  
        deq.append(n+1)

    if n*2 <= right_most and brown[n*2] == 0:
        brown[n*2] = brown[n] + 1
        deq.append(n*2)

for i in range(1,10):
    if brown[cony[i]]<=i:
        print(i)
        break