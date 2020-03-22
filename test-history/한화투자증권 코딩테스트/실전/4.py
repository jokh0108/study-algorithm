# TREE

n = int(input())
tree = {1 : [1]}
# print(tree)
for i in range(2, n+1):
    new_magnet = i
    append_flag = False
    # i == 2 -> 1번, i == 3 -> 2번, ... , i == n -> n-1번 이므로
    # O(N^2)
    for k, v in tree.items():
        r = (v[-1] + new_magnet)**0.5 # root
        if r == int(r):
            v.append(new_magnet)
            append_flag = True
    if not append_flag:
        tree[new_magnet] = [new_magnet]
print(len(tree), end='')