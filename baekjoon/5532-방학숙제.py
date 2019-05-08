from math import ceil

L, A, B, C, D = [int(input()) for _ in range(5)]

print(L - max(ceil(A/C), ceil(B/D)))
