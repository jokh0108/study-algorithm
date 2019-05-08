lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
tc = int(input())
for _ in range(tc):
    N, leng = input().split()
    L = input().split()
    L = sorted(L, key=lambda x: lst.index(x))
    print(N)
    for each in L:
        print(each, end=' ')
    print()
    # print("".join(L))