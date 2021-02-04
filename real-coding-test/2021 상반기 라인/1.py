import collections

def solution(boxes):
    box_num = len(boxes)
    counter = collections.Counter()
    for box in boxes:
        counter.update(collections.Counter(box))
    print(counter)
    full_boxes = list(filter(lambda x: counter[x] == 2, counter))
    print(full_boxes)

    if box_num >- len(full_boxes):
        return box_num - len(full_boxes)
    return 0

print(solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]))