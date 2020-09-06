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

def partition(arr, start, end):
    arr[start], arr[end // 2] = arr[end // 2], arr[start]
    pivot = arr[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and pivot <= arr[right]:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right


def qsort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        qsort(arr, start, pivot - 1)
        qsort(arr, pivot + 1, end)
    return arr

# def qsort(array, left, right):
#     if left < right:
#         sentinel = partition(array, left, right)
#         qsort(array, left, sentinel-1)
#         qsort(array, sentinel+1, right)
#
#
# def partition(array, left, right):
#     # Lomuto 파티션
#     # i = left - 1
#     # pivot = array[right]
#     # for j in range(left, right):
#     #     if array[j] <= pivot:
#     #         i += 1
#     #         array[i], array[j] = array[j], array[i]
#     #
#     # array[i+1], array[right] = array[right], array[i+1]
#     # return i + 1
#
#     # hoare 파티션
#     pivot = sorted([array[left], array[right], array[right//2]])[1]
#     i = left + 1
#     j = right
#     while i <= j:
#         while i <= j and array[i] <= pivot:
#             i += 1
#         while i <= j and array[j] >= pivot:
#             j -= 1
#         if i <= j:
#             array[i], array[j] = array[j], array[i]
#     array[left], array[j] = array[j], array[left]
#     return j


T = int(input())
for t in range(T):

    N = int(input())
    array = deque(map(int, input().split()))
    cases = [0]
    # print( arr)
    # array = merge_sort(cases, array)
    qsort(array, 0, N-1)
    # print(array)


    print("#%d" % (t+1), array[N//2])
