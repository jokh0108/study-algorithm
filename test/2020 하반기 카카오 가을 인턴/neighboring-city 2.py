def closestStraightCity(c, x, y, q):
    city_coordinates = {}  # city: (x, y)
    share_x = {}  # x: {neighboring cities}
    share_y = {}  # y: {neighboring cities}
    for i in range(len(c)):
        city_coordinates[c[i]] = (x[i], y[i])
        if x[i] not in share_x:
            share_x[x[i]] = {c[i]}
        else:
            share_x[x[i]].add(c[i])
        if y[i] not in share_y:
            share_y[y[i]] = {c[i]}
        else:
            share_y[y[i]].add(c[i])
    # print(city_coordinates, share_x, share_y, sep='\n')

    answer = []
    distances = {}  # (a, b): d and (b, a): d
    for q_city in q:
        neighbors = []
        q_x, q_y = city_coordinates[q_city]
        # print(q_city, q_x, q_y)

        neighbors_x = share_x[q_x] - {q_city}
        # print(neighbors_x)
        for neighbor in neighbors_x:
            _, n_y = city_coordinates[neighbor]
            neighbors.append((neighbor, abs(q_y - n_y)))

        neighbors_y = share_y[q_y] - {q_city}
        # print(neighbors_y)
        for neighbor in neighbors_y:
            n_x, _ = city_coordinates[neighbor]
            neighbors.append((neighbor, abs(q_x - n_x)))

        # print(neighbors)
        if neighbors:
            nearest_city_name = sorted(neighbors, key=lambda x: (x[1], x[0]))[0][0]
            answer.append(nearest_city_name)
        else:
            answer.append('NONE')
    # print(answer)

    return answer




