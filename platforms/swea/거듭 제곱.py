def recur(N, M):
    if M == 1:
        return N
    return N * recur(N, M-1)
for i in range(1, 11):
    input()
    N, M = map(int, input().split())
    ans = recur(N, M)
    print("#%d"%i, ans)