import bisect
import pprint
import collections

def solution(info, query):

    answer= []
    applicants = []
    for _, applicant in enumerate(info):
        language, position, level, food, score = applicant.split()
        score = int(score)
        applicants.append([language, position, level, food, score])
    # pprint.pprint(applicants)
    # pprint.pprint(applicants)

    # print(bisect.bisect_left(list('abcfg'), 'a'))
    # print(bisect.bisect_left(list('abcfg'), 'b'))
    # print(bisect.bisect_left(list('abcfg'), 'c'))
    # print(bisect.bisect_left(list('abcfg'), 'd'))
    # print(bisect.bisect_left(list('abcfg'), 'e'))
    # print(bisect.bisect_left(list('abcfg'), 'f'))
    # print(bisect.bisect_left(list('abcfg'), 'g'))
    
    # print()
    for q in query:
        language, position, level, food, query_score = filter(lambda x: x != 'and', q.split())
        query_score = int(query_score)

        remained_applicants = applicants[:]

        # query_score
        remained_applicants = sorted(remained_applicants, key=lambda x: (x[-1]))
        # print('after sorted')
        # pprint.pprint(remained_applicants)
        target = bisect.bisect_left([x[-1] for x in remained_applicants], query_score)
        # print(target, query_score)
        remained_applicants = [remained_applicants[:] for remained_applicants in remained_applicants[target:]]
        # pprint.pprint(remained_applicants)

        # food
        if food != '-':
            remained_applicants = sorted(remained_applicants, key=lambda x: (x[-2]))
            # print('after sorted, food')
            # pprint.pprint(remained_applicants)
            target_start = bisect.bisect_left([x[-2] for x in remained_applicants], food)
            target_end = bisect.bisect_right([x[-2] for x in remained_applicants], food)
            # print(target_start, target_end, food)
            remained_applicants = [remained_applicants[:] for remained_applicants in remained_applicants[target_start:target_end]]
            # pprint.pprint(remained_applicants)

        # level
        if level != '-':
            remained_applicants = sorted(remained_applicants, key=lambda x: (x[-3]))
            # print('after sorted, level')
            # pprint.pprint(remained_applicants)
            target_start = bisect.bisect_left([x[-3] for x in remained_applicants], level)
            target_end = bisect.bisect_right([x[-3] for x in remained_applicants], level)
            # print(target_start, target_end, level)
            remained_applicants = [remained_applicants[:] for remained_applicants in remained_applicants[target_start:target_end]]
            # pprint.pprint(remained_applicants)

        # position
        if position != '-':
            remained_applicants = sorted(remained_applicants, key=lambda x: (x[-4]))
            # print('after sorted, position')
            # pprint.pprint(remained_applicants)
            target_start = bisect.bisect_left([x[-4] for x in remained_applicants], position)
            target_end = bisect.bisect_right([x[-4] for x in remained_applicants], position)
            # print(target_start, target_end, position)
            remained_applicants = [remained_applicants[:] for remained_applicants in remained_applicants[target_start:target_end]]
            # pprint.pprint(remained_applicants)

        # language
        if language != '-':
            remained_applicants = sorted(remained_applicants, key=lambda x: (x[-5]))
            # print('after sorted, language')
            # pprint.pprint(remained_applicants)
            target_start = bisect.bisect_left([x[-5] for x in remained_applicants], language)
            target_end = bisect.bisect_right([x[-5] for x in remained_applicants], language)
            # print(target_start, target_end, language)
            remained_applicants = [remained_applicants[:] for remained_applicants in remained_applicants[target_start:target_end]]
            # pprint.pprint(remained_applicants)

        answer.append(len(remained_applicants))

    return answer

print(solution(
    [
        "java backend junior pizza 150", 
        "python frontend senior chicken 210", 
        "python frontend senior chicken 150", 
        "cpp backend senior pizza 260", 
        "java backend junior chicken 80", 
        "python backend senior chicken 50"
    ], 
    [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150"
     ]
))
