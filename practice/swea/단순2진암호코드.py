code = ["0001101","0011001","0010011","0111101","0100011","0110001","0101111","0111011","0110111","0001011"]
code = {code[i]:i for i in range(len(code))}
# print(code)
tc = int(input())
for i in range(tc):
    N, M = map(int, input().split())
    incode = ""
    for _ in range(N):
        line = input()
        if "1" in line:
            incode = line
    # print(incode)
    for j in range(len(incode)):
        if incode[j:j+7] in code:
            inincode = incode[j:j+56]
            inincode = [inincode[j:j+7] for j in range(0, len(inincode), 7)]
            isCode=True
            # print(inincode)
            for each in inincode:
                if code.get(each) == None:
                    isCode = False
                    break
            if isCode:     
                break
    # print(inincode)
    lst = []
    ans = 0
    for j in range(len(inincode)):
        lst.append(code[inincode[j]])
        # print(lst)
    if (((lst[0] + lst[2] + lst[4] + lst[6])*3 + lst[1]+lst[3]+lst[5]+lst[7]) % 10) == 0:
        ans = sum(lst)
            

    print("#%d"%(i+1), ans)