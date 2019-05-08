def cryptInsert(idx, num):
    for i in range(num):
        crypt.insert(idx + i, command.popleft())
def cryptDelete(idx, num):
    for _ in range(num):
        del crypt[idx]
    pass
# def commandResize(num):
#     for _ in range(num):
#         command.popleft()

def printCrypt(lst):
    for i in range(10):
        print(lst[i], end=" ")
    print()

from collections import deque
for i in range(1, 11):
    input()
    crypt = deque(input().split())
    # print(crypt)
    input()
    command = deque(input().split())

    while command:
        # print("command : ",command)
        oneCommmand = command.popleft()
        idx = int(command.popleft())
        num = int(command.popleft())
        if oneCommmand == 'I':
            cryptInsert(idx, num)
        elif oneCommmand == 'D':
            cryptDelete(idx, num)
        # print("crypt : ",crypt)

    print("#%d"%i, end = " ")
    printCrypt(crypt)