
N = int(input())
answer = set()
for i in range(0, 10):
    if i !=0:
        answer.add(i)
    for j in range(-i,10-i):
        Han = i
        E = 10
        high = Han + j
        for k in range(len(str(N))-1):
            if 0 < high < 10:
                Han += high * E
               # print(Han)
                answer.add(Han)
                high = high + j
                E = E * 10

answer = sorted(answer)
#print(answer)
# print(answer)
for i in range(len(answer)):
   # print(answer[i])
    if answer[i] > N:
        break
if i == len(answer)-1:
    i +=1
answer = answer[:i]
#print(answer)
print(len(answer))