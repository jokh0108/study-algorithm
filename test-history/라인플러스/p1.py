# N = int(input())
# divisors = []
# for i in range(1, int(N**0.5)+1):
#     if N % i == 0:
#         divisors.append(i)
#         if i != N // i:
#             divisors.append(N // i)

# divisors = sorted(divisors)
# # print(divisors)
# leng = len(divisors)
# if leng % 2 == 0:
#     print(abs(divisors[leng // 2-1] - divisors[leng//2]))
# else:
#     print(0)

N = int(input())

if N**0.5 == int(N**0.5):
    print(0)
else:
    for i in range(int(N**0.5), 0,-1):
        # print(i)
        if N % i == 0:
            print(abs(N // i - i))
            break



# divisors = []
# for i in range(1, int(N**0.5)+1):
#     if N % i == 0:
#         divisors.append(i)
#         if i != N // i:
#             divisors.append(N // i)

# divisors = sorted(divisors)
# # print(divisors)
# leng = len(divisors)
# if leng % 2 == 0:
#     print(abs(divisors[leng // 2-1] - divisors[leng//2]))
# else:
#     print(0)
