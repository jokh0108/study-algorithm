# from collections import deque
# l = [x for x in range(1, int(input())+1)]
# deq = deque(l)
# while True and len(deq) > 1:
#     # if len(deq) < 10 :
#     #     print(deq, len(deq))
#     # print(deq)
#     deq.popleft()
#     if len(deq) == 1:
#         break
#     deq.append(deq.popleft())
# print(deq[0])

from math import *
def ans(N):
    l = log2(N)
    if l.is_integer():
        return N
    else:
        base = 2**floor(l)
        return (2 * (N % base))


print(ans(int(input())))
# for i in range(1, 20):
#     print(ans(i))
