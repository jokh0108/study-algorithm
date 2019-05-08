# N = int(input())
# ans = 0
# for _ in range(N):
#     stack = []
#     word = input()
#     for alphabet in word:
#         if stack == []:
#             stack.append(alphabet)
#             # print(stack)
#             continue
#         else:
#             if stack[-1] == alphabet:
#                 stack.pop()
#             else:
#                 stack.append(alphabet)
#             # print(stack)
#     # print(stack)
#     if stack == []:
#         ans += 1
# print(ans)
num_of_good_words = 0

for _ in range(int(input())):
	word, temp = input(), ""
	while word != temp:
		print(word, temp)
		temp = word
		word = word.replace("AA", "").replace("BB","")
	if not word:
		num_of_good_words += 1
print(num_of_good_words)