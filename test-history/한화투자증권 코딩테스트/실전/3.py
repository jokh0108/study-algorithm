# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
x = set()
y = set()
# x, y값이 중복되면 만난다는 얘기이므로
# set으로 중복 제거
# set이 n과 다르면 false
# n과 같으면 true
for _ in range(n):
    x1, y1 = map(int, input().split())
    x.add(x1)
    y.add(y1)
if len(x) == n and len(y) == n:
    print("true", end='')
else:
    print("false", end='')