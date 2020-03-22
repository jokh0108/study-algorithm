
from collections import deque

def cryptInsert(idx, num):
    for i in range(num):
        crypt.insert(idx + i, command.popleft())

def cryptDelete(idx, num):
    for _ in range(num):
        del crypt[idx]
            
def cryptAppend(num):
    for _ in range(num):
        crypt.append(command.popleft())
# def commandResize(num):
#     for _ in range(num):
#         command.popleft()

def printCrypt(lst):
    for i in range(10):
        print(lst[i], end=" ")
    print()
# f = open("input (8).txt", "r")
for i in range(1, 11):
    input()
    crypt = deque(input().split(), 20000)
    input()
    command = deque(input().split(), 20000)

    # N = f.readline()
    # crypt = deque(f.readline().split(), 20000)
    # M = f.readline()
    # command = deque(f.readline().split(), 20000)
    # print(N, M)
    # print(crypt)
    # print(command)
    while command:
        # print("command : ",command)
        oneCommmand = command.popleft()
        idx = int(command.popleft())
        if oneCommmand == 'I':
            num = int(command.popleft())
            cryptInsert(idx, num) 
            # print(len(crypt))
        elif oneCommmand == 'D':
            num = int(command.popleft())
            cryptDelete(idx, num)
            # print(len(crypt))
        elif oneCommmand == 'A':
            num = idx
            cryptAppend(num)
            # print(len(crypt))
        # print("crypt : ",crypt)

    print("#%d"%i, end = " ")
    printCrypt(crypt)