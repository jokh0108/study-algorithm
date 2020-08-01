import sys
import collections
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [[5]* N for _ in range(N)]
tree = [map(int, input().split()) for _ in range(M)]
tree_dict = {(x-1, y-1): collections.Counter({z: 1}) for x, y, z in tree} # Counter == {나이: 개수}

d = [
    (-1, -1), (-1, 0), (-1, +1), (0, -1),
    (0, +1), (+1, -1), (+1, 0), (+1, +1)
]

# print(N, M, K, A, B, tree_dict, sep='\n')

# def print_tree():
#     temp = [[0] * N for _ in range(N)]
#     for (x, y), trees in tree_dict.items():
#         temp[x][y] = trees
#     # print('---tree_map---', *temp, sep='\n')
#     for i in range(N):
#         for j in range(N):
#             # print("%20d(%d)"%(temp[i][j], B[i][j]) if temp[i][j] ==0 else (" "*15, list(temp[i][j].elements()), B[i][j]), end='')
#         # print()
#     # print("tree_dict")
#     s = [(x, y, z) for (x, y), z in tree_dict.items()]
#     s = sorted(s, key=lambda x: (x[0], x[1]))
#     # print(*s, sep='\n')

def spring():
    to_be_deleted = {}
    for (x, y), trees in tree_dict.items():
        tree_items = sorted([(age, tree) for age, tree in trees.items()], key=lambda x:x[0])
        # print(tree_items)
        for age, tree_num in tree_items: # age: 나이, v: 갯수
            if B[x][y] - age < 0:
                if to_be_deleted.get((x, y)):
                    to_be_deleted[(x, y)] += age // 2 * tree_num
                else:
                    to_be_deleted[(x, y)] = age // 2 * tree_num
            else:
                if B[x][y] - age * tree_num >= 0:
                    B[x][y] -= age * tree_num
                    trees[age+1] = tree_num
                else:
                    while B[x][y] - age >= 0:
                        B[x][y] -= age
                        trees[age] -= 1
                        if trees.get(age+1):
                            trees[age+1] +=1
                        else:
                            trees[age+1] = 1
            del trees[age]
                        
                        
            
    # print("\n\nto_be_deleted", to_be_deleted)
    return to_be_deleted

def summer(to_be_deleted):
    for (x, y), nut in to_be_deleted.items():
        B[x][y] += nut

        
def autumn():
    delta = {}
    for (x, y), trees in tree_dict.items():
        for age, tree_num in trees.items(): # age: 나이, v: 갯수
            if age > 1 and age % 5 == 0:
                for dx, dy in d:
                    xx, yy = x + dx, y + dy
                    if 0<= xx <N and 0<= yy <N:
                        if delta.get((xx, yy)):
                            delta[(xx, yy)].update({1: tree_num})
                        else:
                            delta[(xx, yy)] = collections.Counter({1: tree_num})
    for (x, y), trees in delta.items():
        if tree_dict.get((x, y)):
            tree_dict[(x, y)].update(trees)
        else:
            tree_dict[(x, y)] = trees
                
def winter():
    for i in range(N):
        for j in range(N):
            B[i][j] += A[i][j]

for i in range(K):
    t = spring()
    # print("\n\nafter spring", i)
    # print_tree()
    summer(t)
    # print("\n\nafter summer", i)
    # print_tree()
    autumn()
    # print("\n\nafter autumn", i)
    # print_tree()
    winter()
    # print("\n\nafter winter", i)
    # print_tree()

print(sum([sum(x.values()) for x in tree_dict.values()]))
