from collections import deque

def codeGenerate(code):
    step = 1
    while True:
        code.rotate(-1)
        if code[-1]-step > 0:
            code[-1] -= step
        else:
            code[-1] = 0
            # print(code)
            break
        step = (step + 1)
        if step == 6:
            step = 1
        # print(code)
    return list(code)
def printList(lst):
    for each in lst:
        print(each, end =" ")
    print()

test = [10, 6, 12, 8, 9, 4, 1, 3]
d = deque(test)

for i in range(1, 11):
    input()
    ans = codeGenerate(deque(map(int, input().split())))

    print("#%d"%i, end = " ")
    printList(ans)