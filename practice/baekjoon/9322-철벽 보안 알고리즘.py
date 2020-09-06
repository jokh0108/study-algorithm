import sys
input = sys.stdin.readline

case = int(input())

for _ in range(case):
    password = []
    n = int(input())
    pub1 = input().split()
    pub2 = input().split()
    encrypted = input().split()
    decrypted = ""
    for i in range(n):
        idx = pub2.index(pub1[i])
        decrypted += encrypted[idx] + " "
    print(decrypted)
    print('\n')

# import sys
# input=sys.stdin.readline
# for tc in range(int(input())):
#     n=int(input())
#     a=input().split()
#     c={a[i]:i for i in range(n)}
#     a=input().split()
#     d={c[a[i]]:i for i in range(n)}
#     a=input().split()
#     print(' '.join(a[d[i]] for i in range(n)))