from collections import Counter
num_dict = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10
}
num_dict_inv = {v : k for k, v in num_dict.items()}
alpha_dict = {k: Counter(k) for k in num_dict.keys()}
# print(alpha_dict)
t = int(input())

for _ in range(t):
    exp = input()
    A, op, B, _, ans = exp.split()
    A = num_dict[A]
    B = num_dict[B]
    # print(A, op, B, ans)
    if op == '+': real_ans = A + B
    elif op == '-': real_ans = A - B
    else: real_ans = A * B
    # print(real_ans)
    if real_ans < 0 or real_ans > 10:
        print("No")
        continue
    
    # print(num_dict_inv.get(real_ans))
    # print(alpha_dict.get(num_dict_inv.get(real_ans)))
    # print(Counter(ans))
    if alpha_dict.get(num_dict_inv.get(real_ans)) == Counter(ans):
        print("Yes")
    else:
        print("No")
