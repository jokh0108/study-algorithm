def calc(N, A, B, R, C):
    return A * abs(R - C) + B * (N - R * C)

divisors = [[] for _ in range(10**5)]
for i in range(1, 100000):
    for each in range(i, 100000, i):
        divisors[each].append(i)

for i in range(int(input())):
    ans = 0
    m = ((10**5)**2)*3
    N, A, B = map(int, input().split())
    for num in range(N, 0, -1):
        nextMidIdx = midIdx = len(divisors[num])//2
        if len(divisors[num]) % 2 == 0:
            midIdx -= 1
        val = calc(N,A,B,divisors[num][midIdx],divisors[num][nextMidIdx])
        if m > val:
            m = val
    print("#%d" % (i+1), m)
