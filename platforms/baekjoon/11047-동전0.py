N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]

# print(coins)
cnt = 0
idx = -1
while K > 0:
    if coins[idx] > K:
        idx -= 1
    else:
        cnt += K // coins[idx]
        K = K % coins[idx]
        #print(idx, K)
print(cnt)