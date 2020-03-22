from collections import deque

def findHall(s, k):
    s = list(s)
    # print(s)
    for i in range(len(s) - k):
        window = s[i:i+k]
        step = 0
        for j in range(k-1):
            step += window[j+1] - window[j]
        if step == k:
            return True
    return False

def solution(stones, k):
    answer = 0
    # print(stones)
    stones_dict = {}
    for idx, v in enumerate(stones):
        if not stones_dict.get(v):
            stones_dict[v] = {idx}
        else:
            stones_dict[v].add(idx)
    # print(stones_dict)

    keys = sorted(stones_dict.keys())
    s = set()
    cnt = 0
    for i in keys:
        s.update(stones_dict[i])
        cnt += 1
        if findHall(s, k):
            answer = cnt
            break

    return answer + 1


a = solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
print(a)
