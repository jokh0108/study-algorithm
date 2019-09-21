from collections import deque
arr = list(map(int, input().split()))
K = int(input())
M = int(input())

# 거리가 가깝다 -> 차의 절대값이 작다

for i in range(len(arr)):
    arr[i] -= K
# arr = sorted(arr, key = lambda x : abs(x))
print(arr)

# 먼저, 연속하는 수들을 찾는 문제이기 때문에 정렬
arr = sorted(arr)
sums = [] 

# M개의 숫자를 묶음으로 생각한다.
# 다음 숫자가 올때 FIFO 방식으로 기존의 숫자를 뺄 것이기 때문에
# deque을 사용한다.
d = deque(arr[:M])
print(arr)
print(d)
for i in range(M, len(arr)-M+1):
    s1 = sum(d)
    s2 = sum(d) - d[0] + arr[i]
    # 다음에 올 합이 양수면 이제 증가하기만 하므로
    # 현재가 최소값이다(즉, 가장 가깝다)
    if s2 > 0:
        break
    # 차의 절대값이 더 적은 숫자들을 찾음
    if abs(s1) > abs(s2):
        # K-n 과 K+n 중에서 K-n을 택함
        if d[0] == -arr[i]:
            break
        else:
            d.popleft()
            d.append(arr[i])
    print(d)
print(sum(d) + K * M, end='')

# 정렬 후 연속적 탐색하기 때문에
# O(NlogN)