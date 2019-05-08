def quicksort(x):
    if len(x) <= 1:
        return x

    pivot = x[len(x) // 2]
    less = []
    more = []
    equal = []
    for a in x:
        if len(a) < len(pivot):
            less.append(a)
        elif len(a) > len(pivot):
            more.append(a)
        else:
            equal.append(a)

    equal = sorted(equal)

    return quicksort(less) + equal + quicksort(more)

N = int(input())
s = set([input() for _ in range(N)])
l = quicksort(list(s))

for each in l:
    print(each)
# print(l)