n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
for a, b in sorted(arr, key=lambda x: (x[0], x[1])):
    print(a, b)
