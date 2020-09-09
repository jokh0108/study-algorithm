# def maxDifference(px):
#     # Write your code here
#     answer = 0
#     local_min = 10**6
#     for i in range(len(px)):
#         # print(local_min, px[i])
#         if local_min > px[i]:
#             local_min = px[i]
#         # print(answer , px[i] - local_min)
#         if answer < px[i] - local_min:
#             answer = px[i] - local_min
#     if answer == 0:
#         return -1
#     return answer

def maxDifference(px):
    # Write your code here
    max_diff = -1
    local_min = max(px)+1
    for i in px:
        if i > local_min:
            max_diff = max(max_diff, i - local_min)
        local_min = min(local_min, i)
    return max_diff

print(maxDifference([2, 3, 10, 2, 4, 8, 1]))
print(maxDifference([7, 9, 5, 6, 3, 2]))
print(maxDifference([7, 7, 7]))
