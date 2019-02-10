input()
have = {} 
for x in input().split():
    have[int(x)] = 1
#have = sorted([int(x) for x in input().split()])
input()
target = [int(x) for x in input().split()]

for card in target:
    if have.get(card) == 1:
        print(1, end=' ')
    else:
        print(0, end=' ')