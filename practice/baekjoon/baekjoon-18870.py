n = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(set(arr))
compressed = {v: i for i, v in enumerate(sorted_arr)}
enumerate_arr = list(enumerate(arr))
for x in arr:
    print(compressed[x], end=" ")
