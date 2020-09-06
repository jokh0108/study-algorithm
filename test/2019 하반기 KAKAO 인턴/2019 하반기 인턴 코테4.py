class Node:
    def __init__(self, val, parent):
        self.val = val
        self.parent = parent
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.arr = []

    def setRoot(self, val):
        self.root = Node(val, self.root)

    def find(self, val):
        if self.findNode(self.root, val) is False:
            return False
        else:
            return True

    def findNode(self, currentNode, val):
        if currentNode is None:
            return False
        elif val == currentNode.val:
            return currentNode
        elif val < currentNode.val:
            return self.findNode(currentNode.leftChild, val)
        else:
            return self.findNode(currentNode.rightChild, val)

    def insert(self, val):
        if self.root is None:
            self.setRoot(val)
            self.arr.append(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if val < currentNode.val:
            if currentNode.leftChild:
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val, currentNode)
                self.arr.append(val)
        elif val > currentNode.val:
            if currentNode.rightChild:
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val, currentNode)
                self.arr.append(val)


def solution(k, room_number):
    t = BinarySearchTree()
    for n in room_number:
        currentNode = t.findNode(t.root, n)
        if currentNode:
            empty = 0
            for i in range(n+1, k+1):
                currentNode = t.findNode(t.root, i)
                if not currentNode:
                    t.insert(i)
                    break
        else:
            t.insert(n)
        # print(t.arr)
    return t.arr


a = solution(10, [1, 3, 4, 1, 3, 1])
print(a)
