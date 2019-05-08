# def findMaxIdx(nums):
#     idx = 0
#     M = nums[0]
#     for i in range(1, len(nums)):
#         if M <= nums[i]:
#             M = nums[i]
#             idx = i
#     return idx
from itertools import combinations

import sys
sys.setrecursionlimit = 10000

def findMAX(nums, changeCount):
    d[int("".join(nums))][changeCount]= True
    changeCount -= 1
    if changeCount >= 0:
        for comb in combinations(range(len((nums))), 2):
            nums[comb[0]], nums[comb[1]] = nums[comb[1]], nums[comb[0]]
            # print(comb, nums)
            if not d[int("".join(nums))][changeCount]:
                findMAX(nums[:], changeCount)
            # case = int("".join(nums))
            # if M < case :
            #     M = case
            #     maxNums = nums
    else:
        pass
tc = int(input())
for i in range(tc):
    d = [[False]*50 for _ in range(1000000)]    
    M = 0
    nums, changeCount = input().split()
    #list
    # nums = list(map(int, nums))
    nums = list(nums)
    #deque 
    ##
    # print(nums)
    changeCount = int(changeCount)
    # while changeCount != 0:
    #     M = findMaxIdx(nums)
    #     m = nums.index(min(nums))
    findMAX(nums[:], changeCount)
    ans = [i for i in range(1000000) if d[i][0]]
    # print(nums)
    print("#%d"%(i+1), max(ans))