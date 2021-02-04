import json
import pprint


def get_summary(data, target_value):
    refined_data = {}
    # pprint.pprint(data)

    for datum in data:
        refined_data[datum['pk']] = [datum['is_active'], datum['parent'], datum['value']]
        if datum['value'] == target_value:
            target_pk, target_is_active, target_parent = datum['pk'], datum['is_active'], datum['parent']
    # pprint.pprint(refined_data)
    summary = []
    pk, is_active, parent, value = target_pk, target_is_active, target_parent, target_value
    level = 1
    while is_active and level <= 3:
        # print(is_active, parent, value)
        level += 1
        summary.append(value)
        if parent:
            is_active, parent, value = refined_data[parent]
        else:
            break
    # print(is_active, parent, value)

    if not summary:
        return "INACTIVE"
    return ">".join(summary[::-1])


data, target_value = input().split('/')
summary = get_summary(json.loads(data), target_value)
print(summary)
