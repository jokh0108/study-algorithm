t = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
flat_list = sorted([item for sublist in t for item in sublist])
print(flat_list)
