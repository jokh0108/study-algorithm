
memo = [-1] * 31
memo[1] = 1
memo[2] = 3
memo[3] = 6

for i in range(4, 31):
    memo[i] = memo[i - 1] * 2 + memo[i - 2] * 3 + memo[i - 3]
    print(memo)

T = int(input())
for i in range(T):
    N = int(input())

    print("#%d"%(i+1), memo[N])


