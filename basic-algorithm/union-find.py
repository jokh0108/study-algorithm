MAX_SIZE = 10
root = [i for i in range(MAX_SIZE)]

print(root)

def find(x):
  if root[x] == x:
    return x
  else:
    return find(root[x])

def union(x, y):
  x = find(x)
  y = find(y)
  root[y] = x


union(1, 6)
union(2, 3)
union(3, 4)
union(1, 5)
union(8, 9)
union(0, 1)
union(7, 3)

print(root)

num_of_disjoint_set = 0
for i, x in enumerate(root):
  if i == x:
    num_of_disjoint_set += 1

print(num_of_disjoint_set)

disjoint_set = {}
for i in range(len(root)):
  parent = find(i)
  if disjoint_set.get(parent):
    disjoint_set[parent].add(i)
  else:
    disjoint_set[parent] = set()
    disjoint_set[parent].add(i)
print(disjoint_set)
