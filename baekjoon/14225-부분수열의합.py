from itertools import combinations

nums = [False]*(100000*20+1)
N = int(input())
S = [int(x) for x in input().split()]

for i in range(1, N+1):
    for each in combinations(S, i):
        # print(sum(each))
        nums[sum(each)] = True
for i in range(1, len(nums)):
    if nums[i] ==False:
        print(i)
        break