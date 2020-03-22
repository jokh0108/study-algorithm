def get_change_num(cur, remain, k, end):
    # cur : 현재 위치
    # remain : 남은 배터리
    # k : 충전 횟수
    global m
    # print(cur, remain, k, end)
    if cur[-1] == end:
        k = k-1
        if m > k:
            # print(m, '->', k)
            m = k
        return

    for j in range(1, remain + 1):
        if cur[-1] + j <= end:
            cur.append(cur[-1] + j)
            get_change_num(cur, battery[cur[-1]], k + 1, end)
            cur.pop()


m = 10000
t = int(input())
for i in range(t):
    m = 10000
    battery = list(map(int, input().split()))
    n = battery[0]-1
    battery = battery[1:] + [0]
    get_change_num([0], battery[0], 0, n)

    print("#%d" % (i + 1), m)
