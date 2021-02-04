# 단어정렬

# def quicksort(x):
#     if len(x) <= 1:
#         return x

#     pivot = x[len(x) // 2]
#     less = []
#     more = []
#     equal = []
#     for a in x:
#         if len(a) < len(pivot):
#             less.append(a)
#         elif len(a) > len(pivot):
#             more.append(a)
#         else:
#             equal.append(a)

#     equal = sorted(equal)

#     return quicksort(less) + equal + quicksort(more)


N = int(input())
words_set = set([input() for _ in range(N)])
sorted_words = sorted(words_set, key=lambda x: (len(x), x))
for word in sorted_words:
    print(word)
