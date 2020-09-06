import math
import pprint

def print_table(name, rating_table):
    print(name)
    for row in rating_table:
        for elem in row:
            print(f'{elem:2.4f}', end='\t\t')
        print()

def print_arr(name, arr):
    print(name)
    for elem in arr:
        if isinstance(elem, float):
            print(f'{elem:2.4f}', end='\t\t')
        else:
            print(f'{elem:>}', end='\t\t')
    print()

# CF Memory-based 타입
num_sim_user_topk = int(input())
num_item_rec_topk = int(input())
num_users = int(input())
num_items = int(input())
num_rows = int(input())

rating_table = [[0.0] * (num_items+1) for _ in range(num_users+1)]



# for similarity
already_rated_map = {}

for _ in range(num_rows):
    user, item, rating = input().split()
    user, item = int(user), int(item)
    if user not in already_rated_map:
        already_rated_map[user] = set([item])
    else:
        already_rated_map[user].add(item)
    rating_table[user][item] = float(rating)
print_table('rating_table', rating_table)
num_reco_users = int(input())
target_users = [int(input()) for _ in range(num_reco_users)]
print(already_rated_map)
# calculate avg
sums = [0.0] * (num_users+1)
cnts = [0] * (num_users+1)
for i in range(1, num_users+1):
    sums[i] = sum(rating_table[i])
    cnts[i] = sum([1 if e != 0.0 else 0 for e in rating_table[i]])
print_arr('sums', sums)
print_arr('cnts', cnts)
avg_rating_list = [sums[i] / cnts[i] if cnts[i] != 0 else 0.0 for i in range(num_users+1)]
print_arr('avg_rating_list', avg_rating_list)


def euclidean_distance(v):
    return sum([r_xi ** 2 for r_xi in v]) ** 0.5

def dot_product(v1, v2):
    return sum([r_xi * r_yi for r_xi, r_yi in zip(v1, v2)])

# (2)
euclidean_distance_list = [0.0] * (num_users+1)
for i in range(1, num_users+1):
    euclidean_distance_list[i] = euclidean_distance(rating_table[i])
print_arr('euclidean_distance_list', euclidean_distance_list)

dot_product_table = [[0.0] * (num_users+1) for _ in range(num_users+1)]
for x in range(num_users+1):
    for y in range(x+1, num_users+1):
        dot_product_table[x][y] = dot_product_table[y][x] = dot_product(rating_table[x], rating_table[y])
print_table('dot_product_table',dot_product_table)

simil_table = [[0.0] * (num_users+1) for _ in range(num_users+1)]
for x in range(1, num_users+1):
    for y in range(x+1, num_users+1):
        if euclidean_distance_list[x] * euclidean_distance_list[y] != 0.0:
            simil_table[x][y] = simil_table[y][x] = dot_product_table[x][y] / (euclidean_distance_list[x] * euclidean_distance_list[y])
print_table('simil_table',simil_table)

simil_set = {}
for user in range(1, num_users+1):
    for item in range(1, num_items+1):
        if rating_table[user][item] != 0.0:
            continue
        f = lambda x: x[1] > 0.0
        U_prime = sorted(filter(f, [(other_user, simil) for other_user, simil in enumerate(simil_table[user])]), key=lambda x: -x[1])[:num_sim_user_topk]
        print(U_prime)
        simil_set[user] = U_prime

        simil_abs_sum = sum([abs(simil) for _, simil in U_prime])
        k = 1 / simil_abs_sum if simil_abs_sum > 0.0 else 0.0
        rating_table[user][item] = avg_rating_list[user] + k * sum([simil * (rating_table[other_user][item] - avg_rating_list[user]) if item in already_rated_map[other_user] else 0.0 for other_user, simil in U_prime])

print_table('rating_table',rating_table)
pprint.pprint(simil_set)
pprint.pprint(already_rated_map)


for target_user in target_users:
    row = rating_table[target_user]
    simil_users = [simil_user for simil_user, _ in simil_set[target_user]]
    # print(simil_users)
    items_rated_by_simil_users = set()
    for simil_user in simil_users:
        items_rated_by_simil_users |= already_rated_map[simil_user]
    items_rated_by_simil_users -= already_rated_map[target_user]
    # print(items_rated_by_simil_users)
    recomended_items = [(item, row[item]) for item in items_rated_by_simil_users]
    # print(recomended_items)
    recomended_items = list(filter(lambda x: x[0] not in simil_set[target_user], recomended_items))
    # print(recomended_items)
    recomended_items = sorted(recomended_items, key=lambda x: -x[1])
    print(*[i for i, r in recomended_items][:num_item_rec_topk])
