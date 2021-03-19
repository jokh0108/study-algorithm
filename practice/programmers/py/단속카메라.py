def solution(routes):
    answer = 1
    routes = sorted(routes)
    camera_pos = routes[0][1]
    for i in range(len(routes)-1):
        if camera_pos > routes[i][1]:
            camera_pos = routes[i][1]
        if camera_pos < routes[i+1][0]:
            answer += 1
            camera_pos = routes[i+1][1]
    return answer


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))

[[-2, -1], [1, 2], [-3, 0]]
[[0, 0]]
[[0, 1], [0, 1], [1, 2]]
[[0, 1], [2, 3], [4, 5], [6, 7]]
[[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
[[-20, 15], [-20, -15], [-14, -5], [-18, -13], [-5, -3]]
