def sum_matrix(m):
    return sum([sum(row) for row in m])


def can_compress(m):
    w = len(m)
    s = sum_matrix(m)
    return s == 0 or s == w**2


def solution(arr):
    w = 1
    n = len(arr)
    one = sum_matrix(arr)
    zero = n**2 - one
    while w <= n:
        for i in range(0, n, w):
            for j in range(0, n, w):
                sub_matrix = [row[j:j+w]for row in arr[i:i+w]]
                # print("sub_matrix", *sub_matrix, sep='\n')
                if w >= 2 and can_compress(sub_matrix) and sub_matrix[0][0] == 1:
                    one -= 3
                if w >= 2 and can_compress(sub_matrix) and sub_matrix[0][0] == 0:
                    zero -= 3
                # print(zero, one)
        w *= 2
    return [zero, one]


# print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [
      0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]))
