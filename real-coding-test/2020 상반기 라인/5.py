def solution(dataSource, tags):
    answer = []
    tags = set(tags)
    result = {}
    for row in dataSource:
        doc, doc_tags = row[0], set(row[1:])
        print(doc, doc_tags)
        print(tags, doc_tags, tags & doc_tags)
        result[doc] = len(tags & doc_tags)
    print(result)
    result_arr = sorted([(doc, tag_num) for doc, tag_num in result.items() if tag_num > 0], key=lambda x:(-x[1], x[0]))
    print(result_arr)
    return [doc for doc, num in result_arr][:10]

print(solution([
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
], ["t1", "t2", "t3"]))