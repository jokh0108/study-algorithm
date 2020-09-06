from random import randrange
def bubbleSort(x, n):
    length = len(x) - 1
    for i in range(length):
        for j in range(length-i):
            shorter = min(len(x[j]), len(x[j+1]))
            for k in range(n , shorter):
                if x[j][k] > x[j+1][k]:
                    x[j], x[j+1] = x[j+1], x[j]
                    break
                elif x[j][k] == x[j+1][k]:
                    if x[j] > x[j+1]:
                        x[j], x[j+1] = x[j+1], x[j]
                        break
    return x

def solution(strings, n):
    return bubbleSort(strings, n)

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))
print(solution(["".join([chr(randrange(ord('a'), ord('z'))) for _ in range(randrange(3, 7))]) for _ in range(10)], 2))