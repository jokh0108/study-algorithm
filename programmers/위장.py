from itertools import combinations
def solution(clothes):
    product = 1
    d = {}
    for k, v in clothes:
        if d.get(v) == None:
            d[v]=1
        else:
            d[v]+=1
    print(d)
    for x in d.values():
        product = product *(x +1)
    return product - 1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], 
["green_turban", "headgear"]])