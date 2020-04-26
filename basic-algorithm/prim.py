adjacent_list = []
adjacent_list.append((1, 4, 4))
adjacent_list.append((1, 2, 6))
adjacent_list.append((2, 3, 5))
adjacent_list.append((2, 4, 3))
adjacent_list.append((2, 5, 6))
adjacent_list.append((2, 6, 8))
adjacent_list.append((3, 6, 8))
adjacent_list.append((4, 5, 9))
adjacent_list.append((5, 6, 5))

EDGE_NUM = 6

print(*adjacent_list, sep='\n')

adjacent_matrix = [[0]*EDGE_NUM for _ in range(EDGE_NUM)]

for info in adjacent_list:
    x, y, cost = info
    adjacent_matrix[x][y] = cost
    adjacent_matrix[y][x] = cost

print(*adjacent_matrix, sep='\n')


def find_min_cost_and_index(arr):
    cost, index = 10**13, 0
    for i in range(len(arr)):
        if arr[i] != 0 and cost > arr[i]:
            index = i
            cost = arr[i]
    return cost, index


# TODO: Not completed
MST_set = {0}
while len(MST_set) < EDGE_NUM:
    cost = 10**13
    for x in MST_set:
        min_cost, index = find_min_cost_and_index(adjacent_matrix[x])
