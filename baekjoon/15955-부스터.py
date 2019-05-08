#19:44
N, Q = map(int, input().split())
checkPoint = [0]
query = []
for _ in range(N):
    checkPoint.append(tuple(map(int, input().split())))
print(checkPoint)
for _ in range(Q):
    query.append(tuple(map(int, input().split())))
print(query)
