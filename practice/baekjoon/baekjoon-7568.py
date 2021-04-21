N = int(input())

people = [list(map(int, input().split())) for _ in range(N)]

for i, (p, q) in enumerate(people):
    count = 0
    for j, (x, y) in enumerate(people):
        if i == j:
            continue
        if x > p and y > q:
            count += 1
    print(count + 1, end=" ")
print()
