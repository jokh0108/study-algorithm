import collections
def solution(votes, k):
    counter = collections.Counter(votes)
    top_k = counter.most_common(k)
    top_k_votes = sum([vote for _, vote in top_k])

    votes_counts = sorted(list(counter.items()), key=lambda x: (-x[1], x[0]))
    acc = 0
    last_name = votes_counts[-1][0]
    while True:
        name, vote = votes_counts.pop()
        acc += vote
        if acc >= top_k_votes:
            break
        last_name = name
        
    return last_name

print(solution(["AVANT", "PRIDO", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "AVANT", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "SOULFUL", "AVANT", "SANTA"], 2))
print(solution(["AAD", "AAA", "AAC", "AAB"], 4))