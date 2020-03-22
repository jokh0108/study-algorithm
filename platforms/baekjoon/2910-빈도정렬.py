from collections import Counter
import random
N, C = map(int, input().split())
arr = Counter(map(int, input().split()))
# arr = Counter([random.randrange(1, 10) for _ in range(100)])
# print(arr)
for each in sorted(arr.items(),key = lambda x : x[1], reverse=True):
    for i in range(each[1]):
        print(each[0], end=' ')