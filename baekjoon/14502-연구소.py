from itertools import combinations

N, M = map(int, input().split())
init = []
afterWall = []
indexOfVirus = []
indexOfEmpty = []
Graph = []
cnt_1 = 3


def initGraph():
    for row in range(N):
        for col in range(M):
            NEWS = [-1]*4
            if row - 1 >= 0:
                NEWS[0] = (row-1)*M+col
            if col - 1 >= 0:
                NEWS[1] = row * M + (col - 1)
            if col + 1 < M:
                NEWS[2] = row * M + (col + 1)
            if row + 1 < N:
                NEWS[3] = (row+1)*M+col
            node = row * M + col
            if afterWall[node] != 1:
                for each in NEWS:
                    if each != -1:
                        if afterWall[each] == 0:
                            Graph[node].append(each)

def changeGraph(changed):
   # print(changed)
    s = set()
    for each in list(changed):
        s.add(each)
        row = each // M
        col = each % M
        NEWS = [-1]*4
        if row - 1 >= 0:
            NEWS[0] = (row-1)*M+col
        if col - 1 >= 0:
            NEWS[1] = row * M + (col - 1)
        if col + 1 < M:
            NEWS[2] = row * M + (col + 1)
        if row + 1 < N:
            NEWS[3] = (row+1)*M+col
        for near in NEWS:
            if near != -1:
                s.add(near)

    for each in list(s): 
        row = each // M
        col = each % M
        NEWS = [-1]*4
        if row - 1 >= 0:
            NEWS[0] = (row-1)*M+col
        if col - 1 >= 0:
            NEWS[1] = row * M + (col - 1)
        if col + 1 < M:
            NEWS[2] = row * M + (col + 1)
        if row + 1 < N:
            NEWS[3] = (row+1)*M+col
        Graph[each].clear()
        if afterWall[each] != 1:
            for near in NEWS:
                if near != -1:
                    if afterWall[near] == 0:
                        Graph[each].append(near)


def printMap():
    for row in range(N):
        for col in range(M):
            node = row * M + col
            print(afterWall[node], end=' ')
        print()
    print()


def dfs(v, virusList):
    cnt.append(0)
    visit[v] = True
    afterWall[v] = 2
    virusList.append(v)
    #print(v, end=' ')
    for each in Graph[v]:
        if visit[each] == False:
            dfs(each, virusList)


for _ in range(N):
    init += [int(x) for x in input().split()]
for row in range(N):
    for col in range(M):
        node = row*M + col
        if init[node] == 0:
            indexOfEmpty.append(node)
        elif init[node] == 1:
            cnt_1 += 1
        else:
            indexOfVirus.append(node)
        Graph.append([])
maximum = -1
before = set()
after = set()
cnt = []
for one, two, three in combinations(indexOfEmpty, 3):
    after = set([one, two, three])
    virusList = []
    visit = [False]*(N*M)
    #initialize map
    afterWall = init[:]
    #set wall
    afterWall[one] = 1
    afterWall[two] = 1
    afterWall[three] = 1
    for i in range(N*M):
        if afterWall[i] != 0:
            visit[i] = True
    #initialize graph
    # print(before, after)
    if before != set():
        Union = before.union(after)
        Inter = before.intersection(after)
        changeGraph(Union.difference(Inter))
    else:
        initGraph()
    # print("\nBefore")
    # printMap()
    for virus in indexOfVirus:
        dfs(virus, virusList)
        #print("virus : ", virusList)
    # print("\nAfter DFS")
    # print(Graph)
    # printMap()
    if maximum < N*M-cnt_1-len(virusList):
        maximum = N*M-cnt_1-len(virusList)
    # print("max :", maximum)
    before = after

print(maximum)
