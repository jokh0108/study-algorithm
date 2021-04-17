import re

N = int(input())
for _ in range(N):
    matched = re.match(r"^(100+1+|01)+$", input())
    print("YES" if matched else "NO")
