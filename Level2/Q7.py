def median(list1):
    list1.sort()

    n = len(list1)
    middle = n // 2

    if n % 2 == 0:
        result = (list1[middle-1] + list1[middle]) / 2
    else: 
        result = list1[middle]
    
    return result

list1 = list(map(int, input(" Enter the list elements separated by space:- ").split()))

result = median(list1)
print(f" Median of the list:- {result}")