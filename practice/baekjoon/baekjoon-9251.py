str1 = "0"+ input()
str2 = "0"+ input()
len1 = len(str1)
len2 = len(str2)
LCSmap = [[0 for _ in range(len1)] for _ in range(len2)]
LCSmax = 0
LCSlen = 0
for row in range(1, len2):
    for col in range(1, len1):
        if str2[row] == str1[col]:
            LCSmax = LCSmap[row-1][col-1]+1
            LCSmap[row][col] = LCSmax
        else:
            LCSmap[row][col] = max(LCSmap[row][col-1], LCSmap[row-1][col])
    if LCSmax > LCSlen:
        LCSlen = LCSmax

# for row in LCSmap:
#     print(row)

print(LCSlen)
