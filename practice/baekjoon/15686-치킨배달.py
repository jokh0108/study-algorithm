import collections
import itertools


def get_ch_and_house(city, n):
    chicks, houses = [], []
    for r in range(n):
        for c in range(n):
            if city[r][c] == 0:
                continue
            elif city[r][c] == 2:
                chicks.append((r, c))
            elif city[r][c] == 1:
                houses.append((r, c))
    return chicks, houses

def get_dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


def solution(n, m, city):
    chicks, houses = get_ch_and_house(city, n)
    # print(chicks, houses)
    min_d = 10000000000
    for c in itertools.combinations(chicks, m):
        # initiation
        house_dict = collections.defaultdict(int)
        for house in houses:
            house_dict[house] = min_d

        # calculation
        for house in house_dict:
            for chick in c:
                dist = get_dist(*house, *chick)
                if house_dict[house] > dist:
                    house_dict[house] = dist
                    # print(house, chick, house_dict)
        min_d = sum(house_dict.values()) if min_d > sum(house_dict.values()) else min_d
    return min_d

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
# print(city)
print(solution(n, m, city))
