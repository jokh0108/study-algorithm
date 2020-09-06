def solution(n, m, k):
    d = [[0] * (151) for _ in range(151)]
    # print(*d,' ', sep='\n')
    answer = -1
    for j in range(1, k+1):
        d[1][j] = 1
    # print(*d, ' ', sep='\n')

    for i in range(2, n+1):
        for j in range(2, m+1):
            cnt = 0
            for w in range(1, k+1):
                if 1 <= j-w <= m:
                    d[i][j] += d[i-1][j-w]
                    cnt += 1
            if cnt > 0:
                d[i][j] = d[i][j] // cnt
    print(*d, ' ', sep='\n')
    print((d[n][m] * 2) % 1000000007)
    return (d[n][m] * 2) % 1000000007

print(solution(3, 8, 4) == 6)
print(solution(10, 6, 5) == 0)
print(solution(2, 10, 4) == 0)
print(solution(50, 150, 20) == 780361386)