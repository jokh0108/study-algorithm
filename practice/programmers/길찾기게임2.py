class Node:
    def __init__(self, val, x, y):
        self.val = val
        self.x = x
        self.y = y
        self.left = None
        self.right = None


class Tree:
    def __init__(self, node):
        self.head = Node(*node)
        self.pre_arr = []
        self.post_arr = []

    def insert(self, node, val, x, y):
        if not node:
            node = Node(val, x, y)
        else:
            if x <= node.x:
                node.left = self.insert(node.left, val, x, y)
            else:
                node.right = self.insert(node.right, val, x, y)
        return node

    def preorder(self, node):
        if node:
            self.pre_arr.append(node.val)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            self.post_arr.append(node.val)


def solution(nodeinfo):
    nodeinfo = sorted([(i+1, x, y) for i, (x, y) in enumerate(nodeinfo)], key=lambda x: x[2], reverse=True)
    print(nodeinfo)
    answer = []
    t = Tree(nodeinfo[0])
    # put in the nodes
    for i in range(1, len(nodeinfo)):
        t.insert(t.head, *nodeinfo[i])

    t.preorder(t.head)
    t.postorder(t.head)

    answer.append(t.pre_arr)
    answer.append(t.post_arr)

    return answer

print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))