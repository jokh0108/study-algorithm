from collections import Counter
from itertools import combinations

pnum = 3
path = f"p4_inputs/input00{pnum}.txt"
f = open(path, 'r')
input = f.readline

num_of_attrs = int(input())
threshold = float(input())
num_of_rows = int(input())

dataset = Counter()
for _ in range(num_of_rows):
    for c in combinations(input().split(','), num_of_attrs):
        dataset[",".join(c)] += 1

for k, v in dataset.items():
    if v / num_of_rows >= threshold:
        print(k)
