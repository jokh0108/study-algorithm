N, M = [int(x) for x in input().split()]
target = [int(x) for x in input().split()]
result = 0
for i in range(len(target)):
    # print(target)
    if abs(N - target[i]) <  abs(1 - target[i]):
        move = N - target[i] + 1
    else:
        move = 1 - target[i]
    result += abs(move)
    # print(move)
    for j in range(len(target)):
        target[j] = (target[j] + move - 1)%N
    N -= 1 
# print(target) 
print(result)