
min_len = 10001

def resolve(num, cards, arr):
    global min_len
    if num < 0:
        return
    elif num == 0:
        min_len = min(min_len, len(arr))
        # print(arr)
    for card in cards:
        if num - card >= 0:
            arr.append(card)
        # print(num, card, arr)
        resolve(num - card, cards, arr[:])
        if arr:
            arr.pop()

def solution(num, cards):
    arr = []
    resolve(num, cards, arr[:])
    return min_len

# print(solution(8, [1, 4, 6]))/
print(solution(18, [1, 2, 5]))
