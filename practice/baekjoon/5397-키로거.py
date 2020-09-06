# Not Completed

# 입력한 순서대로 L (0 <= L <= 1000000)
# 백스페이스 '-'
# 화살표 입력은 <, >

# class Node:
#   def __init__(x):
#     self.val = x
#     self.next = None
#     self.prev = None

# class LinkedList:
#   def __init__():
#     self.head = None
#     self.cur = None
#     self.tail = None

#   def insert(node):
#     self.cur = node
#     self.

# linked_list = LinkedList()

t = int(input())
for _ in range(t):
    stack = []
    top = 0
    string = input()
    for i in range(len(string)):
        if string[i] == '<':
            top -= 1
            if top < 0:
                top = 0
        elif string[i] == '>':
            top += 1
            if top > len(stack):
                top = len(stack)
        elif string[i] == '-':
            stack.pop()
            top -= 1
            if top < 0:
                top = 0
        else:
            stack.insert(top, string[i])
            top += 1
        # print(stack, top)
    print("".join(stack))
