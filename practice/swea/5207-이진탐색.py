def binarySearch(arr, key):
    start = 0
    loc = []
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if key == arr[mid]:
            if check(loc):
                # print("True", arr, key, loc)
                return mid
            else:
                # print("False", arr, key, loc)
                return -1
        elif key < arr[mid]:
            loc.append(-1)
            end = mid - 1
        else:
            loc.append(1)
            start = mid + 1
    # print("False", arr, key, loc)
    return -1


def check(location):
    for i in range(len(location) - 1):
        if location[i] == location[i+1]:
            return False
    return True


T = int(input())
for t in range(T):
    ans = 0
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for b in B:
        result = binarySearch(A, b)
        if result >= 0:
            ans += 1

    print("#%d" % (t+1), ans)
