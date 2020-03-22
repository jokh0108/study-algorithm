import collections
import copy
r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

def my_sort(arr):
    counter = collections.Counter(arr)
    if counter.get(0):
        del counter[0]
    s = list(counter.items())
    s = sorted(s, key=lambda x: (x[1], x[0]))
    ss = []
    for t in s:
        tt = [x for x in t if x != 0]
        ss.extend(tt)
    arr = ss[:100]
    # print( counter, arr)
    return arr

def get_column(mat, i):
    arr = []
    for row in range(len(mat)):
        arr.append(mat[row][i])
    return arr

def get_max_len(mat):
    return max([len(x) for x in mat])

def extend_mat(mat):
    max_len = get_max_len(mat)
    for i in range(len(mat)):
        mat[i].extend([0] * (max_len - len(mat[i])))
        
def transpose(prev_mat):
    new_mat = [[0 for _ in range(len(prev_mat))] for _ in range(len(prev_mat[0]))]
    # print("empty_mat", *new_mat, sep='\n')
    for col in range(len(prev_mat)):
        for row in range(len(prev_mat[0])):
            new_mat[row][col] = prev_mat[col][row]
    return new_mat

# print(0, "th -------A-------", *A, sep='\n')

for i in range(102):
    if r <= len(A) and c <= len(A[0]) and A[r-1][c-1] == k:
        break
    nr, nc = len(A), len(A[0])
    new_mat = []
    # print(nr, nc, nr >= nc)
    if nr >= nc:
        for j in range(nr):
            new_mat.append(my_sort(A[j]))
        extend_mat(new_mat)
        A = copy.deepcopy(new_mat)
    else:
        for j in range(nc):
            col = get_column(A, j)
            new_mat.append(my_sort(col))
        extend_mat(new_mat)
        A = transpose(new_mat)
    del new_mat
    
    # print(str(i+1)+"th -------A-------", *A, sep='\n')

if i <= 100:
    print( i)
else:
    print(-1)
