def selfNumber(n):
    if n < 10000 :
        temp = n
        answer = n
        while temp != 0:
            answer += temp % 10
            temp = temp // 10
       # print(answer)
        #generator[answer] = True
        return answer

s1 = {i for i in range(1, 10000)}
s2 = set()
#generator =[False]*10050
for i in range(1, 10000):
    s2.add(selfNumber(i))
    # if generator[i] == False:
    #     selfNumber(i)
S = sorted(s1-s2)
for s in S:
    print(s)
    # if generator[i] == False and i < 10000:
    #     print(i)