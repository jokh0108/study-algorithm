N = int(input())
arr = [int(input()) for _ in range(N)]
import collections

counter = collections.Counter(arr)
print(int(round(sum(arr) / len(arr))))
print(sorted(arr)[N // 2])

most_commons = sorted(
    [k for k, _ in (filter(lambda x: x[1] == max(counter.values()), counter.items()))]
)
print(most_commons[0] if len(most_commons) <= 1 else most_commons[1])
print(max(arr) - min(arr))
