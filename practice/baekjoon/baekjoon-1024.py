# N, L = map(int, input().split())
# ans = []
# for i in range(L, N+2):
#     mid = N // i + 1
#     half = i // 2
    
#     if mid - half >= 0:
#         if i % 2 == 0 :
#             nums = list(range(mid - half, mid + half))
#         else:
#             nums = list(range(mid - half - 1, mid + half))
#     else:
#         break
#     # print("nums : ", i, nums)
#     if sum(nums) == N :
#         ans.append(nums)
#         # print(*ans, end='\n')
#         break
# if not ans or len(ans[0]) > 100:
#     print(-1)
# else:
#     print(*ans[0], end=' ')

N, L =1001, 2
while L <= N:
    L += 1
    print("N, L = ",N, L)
    ans = []
    for i in range(L, N+2):
        mid = N // i + 1
        half = i // 2
        
        if mid - half >= 0:
            if i % 2 == 0 :
                nums = list(range(mid - half, mid + half))
            else:
                nums = list(range(mid - half - 1, mid + half))
        else:
            break
        print("nums : ", i, nums)
        if sum(nums) == N and len(nums) <= 100:
            ans.append(nums)
            # print(*ans, end='\n')
            break
    if not ans or len(ans[0]) > 100:
        print(-1)
    else:
        print(*ans[0], end=' ')
    print()
