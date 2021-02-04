def solution(n, delivery):
    delivery = sorted(delivery, key=lambda x: (-x[2], x[0], x[1]))
    print(*delivery, sep='\n')
    result = ['?'] * (n+1)
    for x in delivery:
        first, second, delivered = x
        if delivered:
            result[first] = 'O'
            result[second] = 'O'
        else:
            if result[first] == 'O':
                result[second] = 'X'
            elif result[second] == 'O':
                result[first] = 'X'
        print(result)
    return "".join(result)[1:]

print(solution(6, [[1, 3, 1], [3, 5, 0], [5, 4, 0], [2, 5, 0]]))
print(solution(7, [[5, 6, 0], [1, 3, 1], [1, 5, 0], [7, 6, 0], [3, 7, 1], [2, 5, 0]]))