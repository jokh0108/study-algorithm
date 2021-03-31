def solution(m, n, puddles):
    puddles = {tuple(p) for p in puddles}
    d = [[0]*(m+1) for _ in range(n+1)]
    d[1][1] = 1
    print(*d, sep='\n')

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == j == 1 or (j, i) in puddles:  # i, j 주의
                continue
            d[i][j] = (d[i-1][j] + d[i][j-1]) % 1000000007
            print(i, j, d[i][j])
    print(*d, sep='\n')
    return d[n][m] % 1000000007


print(solution(4, 3, [[2, 2]]))
print(solution(8, 5, [[2, 6], [2, 2], [7, 3]]))
# print(solution(43, 50, []))
