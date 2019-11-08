from collections import deque
from itertools import islice

def merge_sort(cases, m):
    if len(m) <= 1:
        return m

    mid = len(m) // 2
    left = deque(islice(m, 0, mid))
    right = deque(islice(m, mid, len(m)))
    # left = m[:mid]
    # right = m[mid:]

    left = merge_sort(cases, left)
    right = merge_sort(cases, right)

    return merge(cases, left, right)


def merge(cases, left, right):
    result = deque()
    if left[-1] > right[-1]:
        cases[0] += 1
        # print(cases)

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.popleft())
        else:
            result.append(right.popleft())
    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    # print(result)
    return result



T = int(input())
for i in range(T):

    N = int(input())
    array = deque(map(int, input().split()))
    cases = [0]
    # print( arr)
    array = merge_sort(cases, array)
    # print(array)


    print("#%d" % (i+1), array[N//2], cases[0])
