def hanoi(n, a, b, c):
    if n == 1:
        print(f"{a} {c}")
        return
    hanoi(n - 1, a, c, b)
    print(f"{a} {c}")
    hanoi(n - 1, b, a, c)


N = int(input())
answer = 1
for _ in range(N - 1):
    answer = 2 * answer + 1
print(answer)
if N <= 20:
    hanoi(N, 1, 2, 3)
