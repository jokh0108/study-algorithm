import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
stack = []
answer = []
i=0
for _ in range(N):
    num = int(input())

    while num > i:
        i += 1
        stack.append(i)
        answer.append("+")
    
    top = stack.pop()
    if top == num:
        answer.append("-")
    else:
        print("NO")
        break
if not stack:
    for each in answer:
        print(each+"\n")