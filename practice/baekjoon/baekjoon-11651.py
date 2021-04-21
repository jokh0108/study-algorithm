import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
for a, b in sorted(arr, key=lambda x: (x[1], x[0])):
    print(a, b)
