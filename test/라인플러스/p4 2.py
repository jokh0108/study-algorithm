from collections import defaultdict
N = 1000
buildings = []
height_dic =defaultdict(list)
for i in range(N):
    height = 1
    buildings.append(height)
    height_dic[height].append(i)
# print(height_dic)
# print(buildings)
M = 0
for rope_len in range(N-1, 0 , -1):
    for left in range(N - rope_len):

        right = left + rope_len
        # print(left, left + rope_len)
        # print("left : ", buildings[left], "right : ", buildings[right])

        lower = min(buildings[left], buildings[right])
        higher = max(buildings[left], buildings[right])
        # print("lower : ", lower, "higher : ", higher)

        middles = []
        for middle in range(lower, higher+1):
            middles.extend(height_dic[middle])
        # print(middles)
        lst = list(filter(lambda x: x > left and x < right, middles))
        # print(lst)
        if lst == []:
            print(rope_len)
            exit()