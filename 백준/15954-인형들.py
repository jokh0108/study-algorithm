import math

N, K = map(int, input().split())
dolls = list(map(int, input().split()))

ans = 10**12
for k in range(K, N+1):
    for i in range(N-k+1):
        m = sum(dolls[i:i+k]) / k
        b = math.sqrt(sum(map(lambda x: (x-m)**2, dolls[i:i+k])) / k)
        if ans > b:
            ans = b
print(ans)

# from itertools import combinations

# for k in range(K, N+1):
#     for c in combinations(dolls, k):
#         print(c)
#         m = sum(c) / k
#         b = sum(map(lambda x: (x-m)**2, c)) / k
#         print(m, b)