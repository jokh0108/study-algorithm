def check(x, x1, y1, x2, y2):
    x = float(x)
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    if x2 != x1:
        return (y2-y1) / (x2-x1) * (x - x1) + y1
    else:
        return y1


def solution(pattern):
    p_to_coordinates = {1: (1, 3), 2: (2, 3), 3: (3, 3),
                  4: (1, 2), 5: (2, 2), 6: (3, 2),
                  7: (1, 1), 8: (2, 1), 9: (3, 1)
                  }
    coordinates_to_p = {(1, 3): 1, (2, 3): 2, (3, 3): 3,
                   (1, 2): 4, (2, 2): 5, (3, 2): 6,
                   (1, 1): 7, (2, 1): 8, (3, 1): 9
                   }
    lines = {}
    for i in range(len(pattern) - 1):
        m = min(pattern[i], pattern[i+1])
        M = max(pattern[i], pattern[i+1])
        lines[(m, M)] = True

    for line in lines.keys():
        x1, y1 = p_to_coordinates[line[0]]
        x2, y2 = p_to_coordinates[line[1]]
        print(x1, y1, x2, y2)
        oneside = set()
        otherside = set()
        for p in coordinates_to_p.keys():
            temp = check(p[0], x1, y1, x2, y2)
            if p[1] >= temp:
                oneside.add(coordinates_to_p[p])
            else: # p[1] < temp
                otherside.add(coordinates_to_p[p])
            print(oneside, otherside)


print(solution(	[1, 2, 5, 8, 9]))
