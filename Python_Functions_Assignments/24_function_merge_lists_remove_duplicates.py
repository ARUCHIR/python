# 24. Function to merge two lists and remove duplicates

def merge_lists(list1, list2):
    result = []

    for item in list1:
        if item not in result:
            result.append(item)

    for item in list2:
        if item not in result:
            result.append(item)

    return result

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print("List 1:", list1)
print("List 2:", list2)
print("Merged list:", merge_lists(list1, list2))
