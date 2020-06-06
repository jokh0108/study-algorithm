def divide(arr, divisor):
    quotient = 0
    for snack_len in arr:
        quotient += snack_len // divisor
    return quotient

def binary_search(arr, left, right, k):
    max_possible_len = 0
    while left <= right:
        mid = (left + right) // 2
        quotient = divide(arr, mid)
        print('left, mid, right, quotient, k, max_possible_len :', left, mid, right, quotient, k, max_possible_len)
        if quotient == k:
            max_possible_len = mid
            left = mid + 1
        elif quotient < k:
            right = mid + 1
        else:
            left = mid - 1
        # *10000을 한 숫자에서 1의 자리 수가 1 차이 나는 경우는 정답에 영향을 주지 않는다.
        if left + 1 == mid == right - 1:
            return max_possible_len
    return max_possible_len


n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(float(input())*(10**11)))
max_len = max(arr)
result = binary_search(arr, 0, max_len, k)
print(f'{float(result) / (10**11):.2f}')
