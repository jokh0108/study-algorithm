N = int(input())

d = [10**6+3] * (10 ** 6 + 1)
d[1] = 0
d[2] = 1
d[3] = 2
for i in range(1, 10**6+1):
    if i+1 <= 10**6:
        d[i+1] = min(d[i+1], d[i] + 1) 
    if i*2 <= 10**6:
        d[i*2] = min(d[i*2], d[i] + 1) 
    if i*3 <= 10**6:
        d[i*3] = min(d[i*3], d[i] + 1)
print(d[N])