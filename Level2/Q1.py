def common_element(list1, list2):
    common = []
    for i in list1:
        if i in list2 and i not in common:
            common.append(i)
        
    return common

list1 = list(map(int, input(" Enter elements of list1 separated by space:- ").split()))
list2 = list(map(int, input(" Enter elements of list2 separated by space:- ").split()))

result = common_element(list1, list2)
print("Common elements:- ", result)