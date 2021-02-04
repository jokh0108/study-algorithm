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



# deque

# from collections import deque
# def isHan(N):
#     if N < 100:
#         return True
#     deq.clear()
#     deq.append((N // 100) % 10)
#     deq.append((N // 10) % 10)
#     deq.append(N % 10)
#     while N // 100 != 0 : #세자리수 이상만
#         # print(_1, _10, _100)
#         #print(deq)
#         if deq[0] - deq[1] != deq[1] - deq[2]:
#             # print("No")
#             return False
#         deq.pop()
#         N = N // 10
#         deq.appendleft((N // 100) % 10)

#     # print("Yes")

#     return True
# deq = deque()
# N = int(input())
# # isHan(N)
# # answer = 0
# answer = []
# for i in range(1,N+1):
#     if isHan(i):
#         if i >1000:
#             print(i)
#         answer.append(i)
# print(len(answer))


# graph

# N = int(input())
# answer = set()
# for i in range(0, 10):
#     if i !=0:
#         answer.add(i)
#     for j in range(-i,10-i):
#         Han = i
#         E = 10
#         high = Han + j
#         for k in range(len(str(N))-1):
#             if 0 < high < 10:
#                 Han += high * E
#                # print(Han)
#                 answer.add(Han)
#                 high = high + j
#                 E = E * 10

# answer = sorted(answer)
# #print(answer)
# # print(answer)
# for i in range(len(answer)):
#    # print(answer[i])
#     if answer[i] > N:
#         break
# if i == len(answer)-1:
#     i +=1
# answer = answer[:i]
# #print(answer)
# print(len(answer))
