import math

def rotate(delta, x, y):
    xx, yy = x - delta, y - delta
    xxx, yyy = -yy, xx
    return round(xxx + delta), round(yyy + delta)

def slide(key_set, N, M, lock_in, lock_out):
    for i in range(N + M - 1):
        for j in range(N + M - 1):
            moved_set = set()
            for k in key_set:
                moved_set.add((k[0] + i, k[1] + j))
            print(lock_in, moved_set, lock_in & moved_set, lock_in & moved_set == lock_in)
            remain = moved_set - lock_in
            if remain & lock_out:
                continue
            if lock_in & moved_set == lock_in:
                return True
    return False

def turn_90degree(M, key):
    turned_key = set()
    for k in key:
        turned_key.add(rotate(M//2, *k))
    return turned_key


# https://wiki.python.org/moin/TimeComplexity
def solution(key, lock):
    answer = True
    lock_in = set()
    N = len(lock)
    M = len(key)
    lock_out = set()
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                lock_in.add((i+(len(key)-1), j+(len(key)-1)))
            else:
                lock_out.add((i+(len(key)-1), j+(len(key)-1)))
    # print(lock_in)
    # print(lock_out)

    # origin
    key_set = set()
    for i in range(M):
        for j in range(M):
            if key[i][j] == 1:
                key_set.add((i, j))
    # print(key_set)
    result = slide(key_set, N, M, lock_in, lock_out)
    if result: return True

    # turn 90 degree
    key_set = turn_90degree(M, key_set)
    # print(key_set)
    result = slide(key_set, N, M, lock_in, lock_out)
    if result: return True

    # turn 90 degree
    key_set = turn_90degree(M, key_set)
    # print(key_set)
    result = slide(key_set, N, M, lock_in, lock_out)
    if result: return True

    # turn 90 degree
    key_set = turn_90degree(M, key_set)
    # print(key_set)
    result = slide(key_set, N, M, lock_in, lock_out)
    if result: return True

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
