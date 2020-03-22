import pprint

T = int(input())
for i in range(T):
    total = 0

    N, M = map(int, input().split())
    containers = sorted(list(map(int, input().split())), reverse=True)
    capacities = sorted(list(map(int, input().split())), reverse=True)
    j, k = 0, 0
    while j < N and k < M:
        if containers[j] <= capacities[k]:
            total += containers[j]
            k += 1
        j += 1
    print("#%d" % (i+1), total)
