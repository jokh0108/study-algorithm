from collections import deque

for i in range(1, 11):
    crypt = deque(input().split()[1])
    j = 1
    while 0 <= len(crypt) and j < len(crypt):
        if crypt[j] == crypt[j-1]:
            del crypt[j]
            del crypt[j-1]
            j -= 1
        else:
            j += 1
    if len(crypt) == 2 and crypt[0] == crypt[1]:
        crypt.clear()

    print("#%d"%i, "".join(crypt)) 