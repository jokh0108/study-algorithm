class BinaryHeap(object):
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        i = len(self)
        parent = i // 2
        while parent > 0:
            if self.items[i] < self.items[parent]:
                self.items[i], self.items[parent] =\
                    self.items[parent], self.items[i]
            i = parent
            parent = i // 2

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()


binaryHeap = BinaryHeap()
print(binaryHeap.insert(3))
print(binaryHeap.items)
print(binaryHeap.insert(5))
print(binaryHeap.items)
print(binaryHeap.insert(8))
print(binaryHeap.items)
print(binaryHeap.insert(6))
print(binaryHeap.items)
print(binaryHeap.insert(10))
print(binaryHeap.items)
print(binaryHeap.insert(2))
print(binaryHeap.items)
