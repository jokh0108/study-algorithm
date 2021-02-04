def getDivisor(N):
    
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            divisors[N].add(i)
            divisors[N].add(N // i)
    divisors[N].remove(N)

divisors = [set() for _ in range(10001)]
A, B = map(int, input().split())
ans = {}
for i in range(A, B+1):
    getDivisor(i)
    if i == sum(divisors[i]):
        print(i, end=' ')