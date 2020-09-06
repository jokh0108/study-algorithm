def first(a):
    if 0 < a <= 1: return 500
    elif 1 < a <= 3: return 300
    elif 3 < a <= 6: return 200
    elif 6 < a <= 10: return 50
    elif 10 < a <= 15: return 30
    elif 15 < a <= 21: return 10
    else: return 0
def second(b):
    if 0 < b <= 1: return 512
    elif 1 < b <= 3: return 256
    elif 3 < b <= 7: return 128
    elif 7 < b <= 15: return 64
    elif 15 < b <= 31: return 32
    else: return 0

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print((first(a) + second(b)) * 10000)
