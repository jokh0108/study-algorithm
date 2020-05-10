# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def compact(arr, indicies):
    return [e for i, e in enumerate(arr) if i not in indicies]

def lerp(x, x1, y1, x2, y2):
    # print(x, x1, y1, x2, y2)
    return (y2-y1) / (x2-x1) * (x-x1) + y1

def solution(n, P, Q):
    if len(P) == 1:
        return P[0]
    if n in Q:
        return P[Q.index(n)]
    if n < Q[0]:
        return lerp(n, Q[0], P[0], Q[1], P[1])
    if n > Q[-1]:
        return lerp(n, Q[-1], P[-1], Q[-2], P[-2])
    for i in range(len(Q)):
        if Q[i] > n:
            return lerp(n, Q[i-1], P[i-1], Q[i], P[i])

n = int(input())
m = int(input())
Q = [int(input()) for _ in range(m)]
input()
P = [float(input()) for _ in range(m)]

disregarding_indices = [i for i, p in enumerate(P) if p <= 0]
Q = compact(Q, disregarding_indices)
P = compact(P, disregarding_indices)

answer = solution(n, P, Q)
answer = math.floor(answer * 100.0 + 0.5) / 100.0
print(answer)
