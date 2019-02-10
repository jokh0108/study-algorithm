def solution(arrA, arrB):
    start = -1
    if len(arrA) != len(arrB):
        return False

    for i in range(len(arrB)):
        if arrA[0] == arrB[i]:
            start = (i+1)%len(arrB)
    if start == -1:
        return False
    for j in range(1, len(arrA)):
        if arrA[j] != arrB[start]:
            return False
        else:
            start = (start + 1)%(len(arrA))
    return True
