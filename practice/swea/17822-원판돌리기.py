def get_targets(base, limit):
    return list(range(base-1, limit, base))

def rotate(disks, targets, step, clockwise):
    if clockwise:
        step = -step
    for idx in targets:
        disks[idx] = disks[idx][step:] + disks[idx][:step]

def get_adjacent_same_nums(disks):
    adjs = []
    for i in range(N):
        if disks[i][0] and disks[i][0] == disks[i][1]:
            adjs.append([[i, 0],[i, 1]])
        if disks[i][0] and disks[i][0] == disks[i][M-1]:
            adjs.append([[i, 0],[i, M-1]])
        if disks[i][M-1] and disks[i][M-1] == disks[i][M-2]:
            adjs.append([[i, M-1],[i, M-2]])
        if disks[i][M-1] and disks[i][M-1] == disks[i][0]:
            adjs.append([[i, M-1],[i, 0]])
    for j in range(M):
        if disks[0][j] and disks[0][j] == disks[1][j]:
            adjs.append([[0, j],[1, j]])
        if disks[N-1][j] and disks[N-1][j] == disks[N-2][j]:
            adjs.append([[N-1,j],[N-2,j]])
    for i in range(N):
        for j in range(1, M-1):
            if disks[i][j] and disks[i][j] == disks[i][j-1]:
                adjs.append([[i, j],[i, j-1]])
            if disks[i][j] and disks[i][j] == disks[i][j+1]:
                adjs.append([[i, j],[i, j+1]])
    for i in range(1, N-1):
        for j in range(M):
            if disks[i][j] and disks[i][j] == disks[i-1][j]:
                adjs.append([[i, j],[i-1, j]])
            if disks[i][j] and disks[i][j] == disks[i+1][j]:
                adjs.append([[i, j],[i+1, j]])
    print(*adjs, sep='\n')
    return adjs

def remove(adjs, disks):
    for adj in adjs:
        for idx in adj:
            disks[idx[0]][idx[1]] = 0

def get_avg_and_change_nums(disks):
    def get_remained():
        total = 0
        for i in range(N):
            for j in range(M):
                if disks[i][j] != 0:
                    total += 1
        return total
    def set_remained():
        for i in range(N):
            for j in range(M):
                if disks[i][j] != 0:
                    if disks[i][j] > avg:
                        disks[i][j] -= 1
                    elif disks[i][j] < avg:
                        disks[i][j] += 1
        
    _sum = sum([sum(disk) for disk in disks])
    total = get_remained()
    if total > 0:
        avg = _sum / total
        # if avg == _sum // total:
        #     avg = _sum // total
        print("_sum, total, avg", _sum, total, avg)
        set_remained()

N, M, T = map(int, input().split())
disks = []
for _ in range(N):
    disks.append(list(map(int, input().split())))

print(*disks, sep='\n')

for _ in range(T):
    x, d, k = list(map(int, input().split()))
    targets = get_targets(x, N)
    print("targets", targets)
    rotate(disks, targets, k, clockwise=True if d==0 else False)
    print("after rotation ", *disks, sep='\n')
    adjs = get_adjacent_same_nums(disks)
    if adjs:
        remove(adjs, disks)
    else:
        get_avg_and_change_nums(disks)
    print("after adj ", *disks, sep='\n')

print(sum([sum(disk) for disk in disks]))