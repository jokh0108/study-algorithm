import sys
sys.setrecursionlimit(10**7)

class Node():

    def __init__(self, x, y, data):
        self.data = data
        self.x = x
        self.y = y
        self.left = self.right = None

class Tree():
    def __init__(self):
        self.root = None

    def insert(self, x, y, data):
        self.root = self._insert_value(self.root, x, y, data)
        return self.root is not None

    def _insert_value(self, node, x, y, data):
        if node is None:
            node = Node(x, y, data)
        else:
            if x <= node.x:
                node.left = self._insert_value(node.left, x, y, data)
            else:
                node.right = self._insert_value(node.right, x, y, data)
        return node

    def pre_order_traversal(self):
        def preorder(order, root):
            if root is None:
                pass
            else:
                # print(root.data)
                order.append(root.data)
                preorder(order, root.left)
                preorder(order, root.right)
        order = []
        preorder(order, self.root)
        return order

    def post_order_traversal(self):
        def postorder(order, root):
            if root is None:
                pass
            else:
                postorder(order, root.left)
                postorder(order, root.right)
                # print(root.data)
                order.append(root.data)
        order = []
        postorder(order, self.root)
        return order

def solution(nodeinfo):
    # nodeinfo = [[5, 3]]
    nodeinfo = [node+[i+1] for i, node in enumerate(nodeinfo)]
    # print(nodeinfo)
    nodeinfo = sorted(nodeinfo, key= lambda x: x[0])    
    # print(nodeinfo)
    nodeinfo = sorted(nodeinfo, key= lambda x: x[1], reverse = True)
    # print(nodeinfo)
    t = Tree()
    x, y, data = nodeinfo[0]
    t.root = Node(x, y, data)

    for n in nodeinfo[1:]:
        x, y, data = n
        t.insert(x, y, data)

    answer = []
    res = t.pre_order_traversal()
    answer.append(res)
    res = t.post_order_traversal()
    answer.append(res)
    return answer