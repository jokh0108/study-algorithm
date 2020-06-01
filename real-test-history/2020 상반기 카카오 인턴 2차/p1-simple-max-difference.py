def maxDifference(px):
    # Write your code here
    answer = 0
    local_min = 10**6
    for i in range(len(px)):
        print(local_min, px[i])
        if local_min > px[i]:
            local_min = px[i]
        print(answer , px[i] - local_min)
        if answer < px[i] - local_min:
            answer = px[i] - local_min
    if answer == 0:
        return -1
    return answer
