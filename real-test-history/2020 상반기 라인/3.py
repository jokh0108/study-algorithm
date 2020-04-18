# def solution(road, n):
#     normal = True if road[0] == '1' else False
#     cnt = 1
#     new_road = []
#     for i in range(1, len(road)):
#         if road[i - 1] == road[i]:
#             cnt += 1
#         elif road[i - 1] != road[i]:
#             if not normal:
#                 cnt = -cnt
#             new_road.append(cnt)
#             normal = not normal
#             cnt = 1
#     new_road.append(cnt if normal else -cnt)
#     print(new_road)
#
#     cur_sum = 0
#     answer = 0
#     i, j = 0, 0
#     while i <= j and i < len(new_road) and j < len(new_road):
#         if new_road[j] > 0:
#             cur_sum += new_road[j]
#             if answer < cur_sum:
#                 answer = cur_sum
#         else:
#             if n + new_road[j] >= 0:
#                 n += new_road[j]
#                 cur_sum -= new_road[j]
#                 if answer < cur_sum:
#                     answer = cur_sum
#             else:
#                 n -= new_road[i+1]
#                 cur_sum += new_road[i+1]
#                 cur_sum -= new_road[i]
#                 i += 2
#         j += 1
#
#     return answer
def solution(road, n):
    answer = 0
    i, j = 0, 0
    cnt = 0
    while i <= j and i < len(road) and j < len(road):
        if road[j] == '1':
            cnt += 1
            if answer < cnt:
                answer = cnt
        else:
            if n - 1 >= 0:
                n -= 1
                cnt += 1
                if answer < cnt:
                    answer = cnt
            else:
                if road[i] == '0':
                    n += 1
                cnt -= 1
                i += 1
                continue
        j += 1
    return answer

print(solution("111011110011111011111100011111", 3))
print(solution("001100", 5))