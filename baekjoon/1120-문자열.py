a, b = input().split()

m = 2**32
for i in range(len(b)-len(a)+1):
    diff = 0
    for j in range(i, i+len(a)):
        if b[j] != a[j-i]:
            diff += 1
    if m > diff:
        m = diff
print(m)