def solution(n, works):
    works = sorted(works, reverse = True)
    i = 0
    while n > 0:
        print(n, i, works)
        if works[i] >= works[i+1]:
            works[i] -= 1
            n -= 1
        else:
            i += 1
            if i == len(works)-1:
                works[-1] -= 1
                n -= 1
                if works[-1] == 0:
                    break
                i = 0
    print(n, i, works)
    return sum([work**2 for work in works])

print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(	3, [1, 1]))