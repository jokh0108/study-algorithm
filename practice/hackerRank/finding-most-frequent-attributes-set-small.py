from collections import Counter
from pprint import pprint
from itertools import combinations

num_of_attrs = int(input())
threshold = float(input())
num_of_rows = int(input())

dataset = Counter()
all_attr_val_set = set()
for _ in range(num_of_rows):
    rows = input().split(',')
    for c in combinations(rows, num_of_attrs):
        dataset[",".join(c)] += 1
pprint(dataset)

for k, v in dataset.items():
    if v / num_of_rows >= threshold:
        print(k)
