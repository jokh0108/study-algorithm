N = int(input())
filelist = [input() for _ in range(N)]
ans = []
# print(filelist)
for i in range(len(filelist[0])):
    alphabet = set([x[i] for x in filelist])
    if len(alphabet) == 1:
        ans.append(list(alphabet)[0])
    elif len(alphabet) > 1:
        ans.append("?")
    # print(ans)
print("".join(ans))