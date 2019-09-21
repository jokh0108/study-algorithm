user_input = int(input())
# s = []
# for i in range(3, 1000):
#     if i % 3 == 0 or i % 5 == 0:
#         s.append(i)
# print(sum(s))
    
n3 = user_input // 3
n5 = user_input // 5
n15 = user_input // 15
sum3 = 3* n3 *(n3+1) // 2
sum5 = 5* n5 *(n5+1) // 2
sum15 = 15* n15 *(n15+1) // 2
print(sum3 + sum5 - sum15 - user_input)