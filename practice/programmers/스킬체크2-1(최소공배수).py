# def getPrime(arr):
def solution(arr):
    ans = 1
    while True:
        # p = getPrime(arr):
        M = max(arr)
        last = [False] * len(arr)
        for i in range(2, M):
            divisable = [False] * len(arr)
            for j in range(len(arr)):
                if arr[j] % i == 0:
                    divisable[j] = True
            if len([1 for i in range(len(divisable)) if divisable[i] == True]) >= 2:
                for j in range(len(arr)):
                    if arr[j] % i == 0:
                        arr[j] = arr[j] // i
                ans *= i
                last = divisable
                break
            last = divisable
        if len([1 for i in range(len(last)) if last[i] == True]) < 2:
            for each in arr:
                ans *= each
            return ans


print(solution([1]))
print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))
print(solution([100]))
