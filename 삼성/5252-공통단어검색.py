import pprint

T = int(input())
for i in range(T):
    d = {}
    answer = 0
    N, M = map(int, input().split())
    for _ in range(N):
        d[input()] = 1
    # pprint.pprint(d)
    for _ in range(M):
        a = input()
        # print(a, len(a))
        if d.get(a):
            answer += 1

    print("#%d"%(i+1), answer)


