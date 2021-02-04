from pprint import pprint
# import math

# def simil(x, y): # 1-3, 1-4 (x = 1)

#     s1 = set(rating_data[x].keys())
#     s2 = set(rating_data[y].keys())
#     Ixy = s1 & s2
#     if Ixy == set():
#         similarity_dict[(x, y)] = { "similarity" : 0.0, "id":y}
#         return similarity_dict[(x, y)]
#     # print(s1, s2, Ixy)

#     sum1, sum2, sum3 = [0.0]*3
#     for item in Ixy:
#         temp1 = rating_data[x][item] - avg_rating[x]
#         temp2 = rating_data[y][item] - avg_rating[y]

#         sum1 += temp1 * temp2
#         sum2 += pow(temp1, 2)
#         sum3 += pow(temp2, 2)

#     if sum2 == 0.0 or sum3 == 0.0:
#         similarity_dict[(x, y)] = { "similarity" : 0.0, "id":y}
#         return similarity_dict[(x, y)]

#     sum2 = math.sqrt(sum2)
#     sum3 = math.sqrt(sum3)

#     similarity_dict[(x, y)] = { "similarity" : sum1 / (sum2 * sum3), "id":y}

#     return similarity_dict[(x, y)]

# def predictRating(user, item):

#     avg_rating_of_user = avg_rating[user]

#     U_prime = []
#     the_others = most_similar_users_of[user]
#     for other in the_others: # other -> { "similarity" : ?, "id": ? }
#         if rating_data[other["id"]].get(item):
#             U_prime.append(other)
#     # U_prime = U_prime
#     if len(U_prime) == 0:
#         return {"rating" : 0, "item_id": item}

#     k = getNormalizingFactor(user, U_prime)

#     sigma = 0
#     for other in U_prime:
#         similarity = similarity_dict.get((user, other["id"]))
#         if not similarity:
#             similarity = simil(user, other["id"])
#         similarity_val = similarity["similarity"]
#         # sigma += simil(user, other["id"])["similarity"] * (rating_data[other["id"]][item] - avg_rating[other["id"]])
#         sigma += similarity_val * (rating_data[other["id"]][item] - avg_rating[other["id"]])

#     return {"rating" : avg_rating_of_user + k * sigma, "item_id": item}


# def getNormalizingFactor(user, U_prime):
#     denominator = 0 # 분모
#     # U_prime이 없다면??
#     for other in U_prime:
#         similarity = similarity_dict.get((user, other["id"]))
#         if not similarity:
#             similarity = simil(user, other["id"])
#         similarity_val = similarity["similarity"]
#         # denominator += abs(simil(user, other["id"])["similarity"])
#         denominator += abs(similarity_val)
#     return 1 / denominator

# # CF Memory-based 타입
# num_sim_user_topk = int(input())
# num_item_rec_topk = int(input())
# num_users = int(input())
# num_items = int(input())
# num_rows = int(input())
# rating_data = {}
# for _ in range(num_rows):
#     d = input().split()
#     if not rating_data.get(int(d[0])):
#         rating_data[int(d[0])] = {}
#     rating_data[int(d[0])][int(d[1])] = float(d[2])
# num_reco_users = int(input())
# list_reco_users = [int(input()) for _ in range(num_reco_users)]
# similarity_dict = {}

# # print(num_sim_user_topk) # rating 예측 시 사용할 유사 유저수 2
# # print(num_item_rec_topk) # 각 유저별로 추천해줘야 하는 아이템 개수 2
# # print(num_users) # 해당 테스트 케이스에서 제공되는 데이터에 있는 유저 수 5
# # print(num_items) # 해당 테스트 케이스에서 제공되는 데이터에 있는 데이터 수 10
# # print(num_rows) # 15
# # print(*rating_data, sep='\n')
# # pprint(rating_data)
# # print(num_reco_users) # 추천 결과를 만들어야 할 유저 수 2
# # print(list_reco_users) # 추천 결과를 만들어야 할 유저 ID [1,2]

# # 먼저 각 유저의 평균 레이팅을 구해 놓는다.
# # calculate avg
# avg_rating = {}
# for user in rating_data.keys():
#     size = len(rating_data[user].keys())
#     avg = sum(rating_data[user].values()) / size
#     avg_rating[user] = avg
# # print(avg_rating)

# # 가장 유사한 유저 중 상위에 있는 유저만 고른다
# # 피어슨 유사도 사용한다
# # get U' (the set of the similar users -> top `num_sim_user_topk` users)
# most_similar_users_of = {}
# for user in list_reco_users:
#     simil_list = []
#     for other in rating_data.keys():
#         if user != other:
#             similarity = similarity_dict.get((user, other))
#             if not similarity:
#                 similarity = simil(user, other)
#             simil_list.append(similarity)
#     simil_list = sorted(simil_list, key=lambda x : x["similarity"], reverse= True)
#     simil_list = simil_list[:num_sim_user_topk]
#     most_similar_users_of[user] = simil_list

# # predict
# for user in list_reco_users:
#     target_items = set(set(range(1, num_items+1)) - set(rating_data[user].keys()))
#     reco_list = []
#     for item in target_items:
#         reco_list.append(predictRating(user, item))
#     reco_list = sorted(reco_list, key = lambda x : x["rating"], reverse = True)
#     reco_list = reco_list[:num_item_user_topk]
#     for reco in reco_list:
#         print(reco["item_id"], end =' ')
#     print()


import math

def get_cosine_similarity(x, y):

    s1 = set(ratings_of_user_to_item[x])
    s2 = set(ratings_of_user_to_item[y])
    Ixy = s1 & s2
    if Ixy == set():
        return { "similarity" : 0.0, "user_id":y}

    sum1, sum2, sum3 = [0.0]*3
    for item in Ixy:
        r_xi = ratings_of_user_to_item[x][item]
        r_yi = ratings_of_user_to_item[y][item]
        sum1 += r_xi * r_yi
    for item in s1:
        sum2 += pow(ratings_of_user_to_item[x][item], 2)
    for item in s2:
        sum3 += pow(ratings_of_user_to_item[y][item], 2)

    if sum2 == 0.0 or sum3 == 0.0:
        return { "similarity" : 0.0, "user_id":y}

    sum2 = math.sqrt(sum2)
    sum3 = math.sqrt(sum3)

    return { "similarity" : sum1 / (sum2 * sum3), "user_id":y}

def predictRating(user, item):

    avg_rating_of_user = avg_rating[user]

    U_prime = []
    the_others = most_similar_users_of[user]
    for other in the_others:
        if ratings_of_user_to_item[other["user_id"]].get(item):
            U_prime.append(other)
    if len(U_prime) == 0:
        return {"rating" : 0.0, "item_id": item}

    k = getNormalizingFactor(user, U_prime)

    similarity_sum = 0.0
    for other in U_prime:
        similarity_data = similarity_dict.get((user, other["user_id"]))
        if not similarity_data:
            similarity_data = get_cosine_similarity(user, other["user_id"])
        similarity_val = similarity_data["similarity"]
        similarity_sum += similarity_val * (ratings_of_user_to_item[other["user_id"]][item] - avg_rating[other["user_id"]])

    return {"rating" : avg_rating_of_user + k * similarity_sum, "item_id": item}


def getNormalizingFactor(user, U_prime):
    denominator = 0
    for other in U_prime:
        similarity_data = similarity_dict.get((user, other["user_id"]))
        if not similarity_data:
            similarity_data = get_cosine_similarity(user, other["user_id"])
        similarity_val = similarity_data["similarity"]
        denominator += abs(similarity_val)
    if denominator == 0:
        return 0
    return 1 / denominator

# CF Memory-based 타입
num_sim_user_topk = int(input())
num_item_rec_topk = int(input())
num_users = int(input())
num_items = int(input())
num_rows = int(input())
ratings_of_user_to_item = {}
for _ in range(num_rows):
    user, item, rating = input().split()
    user, item = int(user), int(item)
    if not ratings_of_user_to_item.get(user):
        ratings_of_user_to_item[user] = {}
    ratings_of_user_to_item[user][item] = float(rating)
num_reco_users = int(input())
list_reco_users = [int(input()) for _ in range(num_reco_users)]
similarity_dict = {}

# calculate avg
avg_rating = {}
for user in ratings_of_user_to_item:
    avg = sum(ratings_of_user_to_item[user].values()) / len(ratings_of_user_to_item[user])
    avg_rating[user] = avg

most_similar_users_of = {}
for user in list_reco_users:
    similar_list = []
    for other in ratings_of_user_to_item:
        if user != other:
            similarity_data = similarity_dict.get((user, other))
            if not similarity_data:
                similarity_data = get_cosine_similarity(user, other)
            similarity_dict[(user, other)] = similarity_data
            similar_list.append(similarity_data)
    similar_list = sorted(similar_list, key=lambda x : x["similarity"], reverse= True)
    most_similar_list_of_target = similar_list[:num_sim_user_topk]
    most_similar_users_of[user] = most_similar_list_of_target
pprint(most_similar_users_of)
pprint(similarity_dict)

# predict
for user in list_reco_users:
    target_items = set(set(range(1, num_items+1)) - set(ratings_of_user_to_item[user]))
    reco_list = []
    for item in target_items:
        reco_list.append(predictRating(user, item))
    reco_list = sorted(reco_list, key = lambda x : x["rating"], reverse = True)
    reco_list = reco_list[:num_item_rec_topk]
    for reco in reco_list:
        print(reco["item_id"], end =' ')
    print()
