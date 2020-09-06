def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]


def union(x, y):
    x = find(x)
    y = find(y)
    root[y] = x


def isParentSame(x, y):
    return find(x) == find(y)


adjacent_list = []
adjacent_list.append((1, 4, 4))
adjacent_list.append((1, 2, 6))
adjacent_list.append((2, 3, 5))
adjacent_list.append((2, 4, 3))
adjacent_list.append((2, 5, 7))
adjacent_list.append((2, 6, 8))
adjacent_list.append((3, 6, 8))
adjacent_list.append((4, 5, 9))
adjacent_list.append((5, 6, 11))

print(*adjacent_list, sep='\n')

root = [i for i in range(7)]
print(root)

# Time Complexity : O(eloge)
adjacent_list = sorted(adjacent_list, key=lambda x: x[2])

print(*adjacent_list, sep='\n')

total = 0
for info in adjacent_list:
    x, y, cost = info
    if not isParentSame(x, y):
        total += cost
        union(x, y)
        print(x, y, cost, total, root)
