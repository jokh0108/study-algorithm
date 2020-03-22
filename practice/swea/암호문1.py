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
    command = input().split("I ")
    # print(command)
    for j in range(1, len(command)):
        oneCommand = command[j].split()
        # print(oneCommand)
        for k in range(int(oneCommand[1])):
            crypt.insert(int(oneCommand[0])+k, oneCommand[k+2])
            # print(crypt)
    print("#%d"%i, end = " ")
    printCrypt(crypt)