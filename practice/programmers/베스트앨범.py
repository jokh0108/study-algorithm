def solution(genres, plays):
    d = {}
    answer = []


    for i in range(len(genres)):
        if d.get(genres[i]) == None:
            songs = {}
            songs[i] = plays[i]
            d[genres[i]] = [plays[i],songs]# [sum, dictionary of song #]
        else:
            d[genres[i]][0] += plays[i]
            d[genres[i]][1][i] = plays[i]
    print(d.items())
    genre_sort = sorted(d.items(), key=lambda x:x[1][0], reverse= True)
    for each in genre_sort:
        song_dict = each[1][1]
        play_sort = sorted(song_dict.items(), key=lambda x:x[1], reverse= True)
        answer.append(play_sort[0][0])
        if len(play_sort) > 1:
            answer.append(play_sort[1][0])
    print(answer)
    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
)