import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
stack = []
for _ in range(N):
    command = input().split()
    if len(command) == 2:
        X = int(command[1])
        stack.append(X)
    else:
        if command[0] == 'pop':
            if stack == []:
                print(-1)
            else:
                print(stack.pop())
        if command[0] == 'size':
            print(len(stack))
        if command[0] == 'empty':
            if stack == []:
                print(1)
            else:
                print(0)
        if command[0] == 'top':
            if stack == []:
                print(-1)
            else:
                print(stack[-1])
    # print(stack)
    