from pprint import pprint
from collections import defaultdict
import copy
import math

pnum = 1

path = f"p4_inputs/input00{pnum}.txt"
f = open(path, 'r')
input = f.readline
###############################################################

# 앞서 2번 문제에서 사용했던 알고리즘을 그대로 사용하면
# 최악의 경우 약 2억 번 정도의 반복을 하기 때문에 타임아웃이 돼서
# 다른 방법을 찾아야 했는데 시험 시간에는 문제를 못 풀었습니다.

# 그래서 시험이 끝나고 개선점을 생각해보니
# 조합이다 보니 많은 부분이 중복되어 카운트돼서
# 시간이 낭비되고 있었습니다.

# 그래서 이전의 데이터의 정답을 저장해놓고
# 다음 attribute가 추가될 때 기존 데이터와 연관지으면 빠르게 풀 수 있을 것 같아서
# dynamic programming으로 풀어봤는데
# 빠르게 풀 수 있습니다.

attrNum = int(input())
threshold = float(input())
rowNum = int(input())

# 제가 푼 방식은 threshold와 데이터 갯수를 미리 곱해놓고
# 이것을 조합의 최소 인원으로 생각했습니다.
# 예를 들어, threshold가 0.6이고, 데이터 갯수가 10이면
# 조합의 최소 인원은 6명이 됩니다.
min_population = math.ceil(threshold * rowNum)
attr_num = list()

# 그리고 데이터를 저장할 때 set이라는 자료구조를 이용해서
# 각 속성의 Value 별로 id를 집합에 포함시켰습니다.
# 예를 들어, age라는 속성에 Middle-aged라는 Value에는
# id 0~5까지 10명 중 6명이 들어가고
# Senior라는 Value에는 id 6~9까지 4명이 들어가도록 저장합니다.

# 그런 다음 기존 조합에 속성의 value를 하나씩 추가할 때
# 기존 조합과 새로운 속성의 value값에 속한 id 집합의 교집합을
# 다음 조합으로 만드는 방식으로 풀었습니다.
dataset = defaultdict(lambda: defaultdict(set))
for id_num in range(rowNum):
    row = input()
    if '\n' in row:
        row = row[:-1]
        # print(row)
    row = row.split(",")
    # row = input().split(",")
    for idx in range(len(row)):
        attr, val = row[idx].split('=')
        if id_num == 0:
            attr_num.append(attr)
        dataset[(idx,)][val].add(id_num)

# pprint(dataset, width=20)
attr_num = list(attr_num)
# print(attr_num)
for a in dataset:
    for v in dataset[a]:
        print(f'{v} : {len(dataset[a][v])} vs. {min_population} {len(dataset[a][v]) >= min_population}')



attrs = list(dataset.keys())
for attr in attrs:
    vals = list(dataset[attr].keys())
    for val in vals:
        if len(dataset[attr][val]) < min_population:
            del dataset[attr][val]
            if not dataset[attr]:
                del dataset[attr]

# pprint(dataset, width=20)

# 자세히
# 이제 기존 조합에 속성을 추가할 때
print()
dataset_copy = copy.deepcopy(dataset)
for i in range(attrNum-1):
    d = defaultdict(lambda: defaultdict(set))
    for a in dataset:
        for v in dataset[a]:
            print(a, ":", len(dataset[a][v]), "vs.", min_population )
    attrs1 = list(dataset.keys())
    attrs2 = list(dataset_copy.keys())
    for attr1 in attrs1:
        for attr2 in attrs2:
            if attr1[-1] < attr2[0]:
                # print(attr1, attr2)
                for val1 in dataset[attr1]:
                    for val2 in dataset_copy[attr2]:
        # 기존 조합에 속한 id 집합과 새로 추가할 속성에 속한 id 집합의 교집합을
        # 다음 조합으로 생각하면서 속성을 추가해갈 것입니다.
        # 이 때 다음 조합의 크기가 최소 인원보다 작으면
        # 제외합니다.
        # 이 부분에서 상당히 많은 부분이 줄어들어
        # 수행시간을 줄이는데 도움을 줄 수 있습니다.
                        s = dataset[attr1][val1] & dataset_copy[attr2][val2]
                        if len(s) >= min_population:
                            d[attr1 + attr2][val1 + ',' + val2] = s
    dataset = d
    print()
# pprint(dataset, width=20)

for a in dataset:
    for v in dataset[a]:
        print(a, ":", len(dataset[a][v]), "vs.", min_population )
ans = []
for attrs in dataset:
    for vals in dataset[attrs]:
        attrs = [attr_num[attr] for attr in attrs]
        vals = vals.split(',')
        length = len(attrs)
        res = ''
        for idx in range(length):
            res += attrs[idx] + '=' + vals[idx] + ','
        res = res[:-1]

        print(res)
        ans.append(res)

f = open(f"p4_inputs/output00{pnum}.txt")
lines = f.readlines()
for i in range(len(lines)):
    if '\n' in lines[i]:
        lines[i] = lines[i][:-1]
    lines[i] = lines[i].split(',')
    lines[i] = sorted(lines[i])
    lines[i] = ",".join(lines[i])
    ans[i] = ans[i].split(',')
    ans[i] = sorted(ans[i])
    ans[i] = ",".join(ans[i])
lines = sorted(lines)
ans = sorted(ans)

for i in range(len(lines)):
    if lines[i] != ans[i]:
        print(False)
    else:
        print(True)


# attribute의 종류가 어떻게 분포되어있느냐에 따라
# 시간복잡도가 달라집니다.

# 그런데 극단적으로 attribute별 value의 종류가 전부다 다르다고하면
# 최악의 경우 6 * 30000 ^ 6 = 최악!!
# 그런데 이 경우는 threshold를 3만분의 1로 정하는 것과 같으므로
# 현실성이 없긴 합니다.

# 그래서 몇 종류 이하는 되어야 하는지 알아보기 위해 계산해봤더니
# attribute별 value의 종류의 수가 x라 했을 때, x가 16개 이하는 되어야
# 1억번의 반복 이하로 들어올 수 있다는 결론을 얻을 수 있었습니다.

# 구하는 식은
# attribute별 value의 종류의 수 즉, x
# 그것의 r 제곱과
# r을 곱했을 때의 횟수가
# 1억 이하다 라는 수식이고
# x값은 r을 1부터 6까지 대입해가면서 구할 수 있었습니다.

# 정확한 시간복잡도는 솔직히 구하기 어렵지만
# O(r*(r*r+1)/2 * (x의 r제곱))
# => O(r*3 * (x의 r제곱))

# ################################################################

# from itertools import combinations
# from collections import Counter
# attrNum = int(input())
# threshold = float(input())
# rowNum = int(input())
# dataset = []
# for i in range(rowNum):
#     row = input().split(",")
#     # print(row)
#     data = dict()
#     for each in row:
#         key, value = each.split('=')
#         data[key] = value

#     dataset.append(data)
# # print(dataset)
# # pprint(dataset,width = 20)
# ans = []
# cnt = 0
# for attr in combinations(dataset[0].keys(), attrNum):
#     # print(attr)
#     records = []
#     for data in dataset:
#         record = str()
#         for each in attr:
#             record += each + "=" + data[each] +","
#             cnt += 1
#         record = record[:-1]
#         records.append(record)
#         # print(record)
#     counter = Counter(records)
#     for each in counter.items():
#         cnt+=1
#         if each[1] / rowNum >= threshold:
#             ans.append(each[0])

# print(cnt)
#     # print()
#     # print(*ans, sep='\n')
#     # print()
#     # pprint(counter, width=20)
#     # print(C, " * ", rowNum, " * ", len(counter), " = ", case)
#     # print()
# # print()
# # print(*ans, sep='\n')
# f = open("p4_inputs/output00" + pnum +".txt")
# print(lines, ans)
# lines = f.readlines()
# for i in range(len(lines)):
#     if '\n' in lines[i]:
#         lines[i] = lines[i][:-1]
#     lines[i] = lines[i].split(',')
#     lines[i] = sorted(lines[i])
#     lines[i] = ",".join(lines[i])
#     if '\n' in ans[i]:
#         ans[i] = ans[i][:-1]
#     ans[i] = ans[i].split(',')
#     ans[i] = sorted(ans[i])
#     ans[i] = ",".join(ans[i])
# lines = sorted(lines)
# ans = sorted(ans)

# for i in range(len(lines)):
#     if lines[i] != ans[i]:
#         print(False)
#     else:
#         print(True)
