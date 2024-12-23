def unique_elements(list1):
    new_list = []
    for i in list1:
        if i not in new_list:
            new_list.append(i)
    return new_list

list1 = list(map(int, input(" Enter elements of list separated by space:- ").split()))

result = unique_elements(list1)

print(" List with unique elements:- ", result)