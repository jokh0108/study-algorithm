# from collections import deque
# from copy import deepcopy
# from math import log2

# def printStar(star):
#     for row in star:
#         for col in row:
#             print(col, end='')
#         print()

# star = deque([
#     deque([' ',' ','*',' ',' ',' ',]),
#     deque([' ','*',' ','*',' ',' ',]),
#     deque(['*','*','*','*','*',' ',])]
# )

# N = int(input())
# height = N
# iteration = int(log2(N//3))
# for i in range(iteration+1):
#     for j in range(len(star)):
#         for k in range(len(star)):
#             print(" ",end='')
#         for k in range(len(star[j])):
#             print(star[j][k],end='')
#         for k in range(len(star)):
#             print(" ",end='')
#         print()
#     for j in range(len(star)):
#         star.append(deque(list(star[j])*2))
# #printStar(star)
from collections import deque
from copy import deepcopy
from math import log2

def printStar(star):
    for row in star:
        for col in row:
            print(col, end='')
        print()

star = deque([
    deque([' ',' ','*',' ',' ',' ',]),
    deque([' ','*',' ','*',' ',' ',]),
    deque(['*','*','*','*','*',' ',])]
)

N = int(input())
height = N
iteration = int(log2(N//3))
for i in range(iteration):
    for j in range(len(star)):
        star.append(deepcopy(star[j]))
        for k in range(len(star[j])-1,-1,-1):
            star[-1].appendleft(star[j][k])
    for j in range(len(star)//2):
        for k in range(len(star)//2):
            star[j].appendleft(' ')
            star[j].append(' ')

printStar(star)
