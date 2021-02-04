user_input = list(map(int, input().split()))
d = {int(n): i for i, n in enumerate([8, 5, 2, 4, 3, 7, 6, 1, 0, 9])}
user_input_index = sorted([(d[n], n) for n in user_input])
sorted_array = [str(n) for _, n in user_input_index]
print(" ".join(sorted_array))