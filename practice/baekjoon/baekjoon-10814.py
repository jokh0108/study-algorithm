n = int(input())
arr = []
for i in range(n):
    age, name = input().split()
    arr.append([i, int(age), name])
for _, age, name in sorted(arr, key=lambda x: (x[1], x[0])):
    print(age, name)
