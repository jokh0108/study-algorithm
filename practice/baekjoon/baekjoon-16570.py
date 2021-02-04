import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

s = set()
for i in range(len(arr)-1):
    if arr[i] == arr[-1]:
        s.add(i)

if s:
    coef = 1
    scopy = set(list(s))
    for i in range(1, len(arr)):
        for j in scopy:
            if arr[j-i] != arr[-1-i]:
                s.remove(j)
        if len(s) > 1:
            coef += 1
            scopy = set(list(s))
        else:
            break
    print(coef, len(scopy))
else:
    print(-1)
