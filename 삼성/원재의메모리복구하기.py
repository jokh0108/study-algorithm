
for i in range(int(input())):
    mem = input()
    ans = int(mem[0])
    for j in range(len(mem)-1):
        if mem[j] != mem[j+1]:
            ans += 1
    print("#%d"%(i+1), ans)