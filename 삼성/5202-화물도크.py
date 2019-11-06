import pprint

T = int(input())
for i in range(T):
    N = int(input())
    times = []
    for _ in range(N):
        times.append(tuple(map(int, input().split())))
    times = sorted(times, key=lambda x: x[1])

    can_be_used = 0
    prev_start, prev_end = 0, 0
    answer = []
    for j in range(N):
        next_start, next_end = times[j]
        if next_start >= prev_end:
            can_be_used += 1
            answer.append((next_start, next_end))
            prev_start = next_start
            prev_end = next_end
    # print(answer)
    print("#%d" % (i+1), can_be_used)
