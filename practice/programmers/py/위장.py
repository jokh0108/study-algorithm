from collections import defaultdict

def solution(clothes):
    product = 1
    clothe_map = defaultdict(int)
    for _, category in clothes:
        clothe_map[category] += 1
    for clothe_count in clothe_map.values():
        product = product * (clothe_count +1)
    return product - 1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], 
["green_turban", "headgear"]])
