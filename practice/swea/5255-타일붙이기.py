t = int(input())

cache = [0] * 31
cache[1] = 1
cache[2] = 3
cache[3] = 6
for i in range(4, 31):
    cache[i] = cache[i-1] + cache[i-2] * 2 + cache[i-3] 
    # cache[i-2] : 2x2 타일을 붙이는 건 2x1 붙이는 것과 중복(세로로 두개)되므로 하나 빼야함

for j in range(t):
    n = int(input())
    print("#%d"%(j+1), cache[n])