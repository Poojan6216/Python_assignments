def access_element(list1, index):
    try:
        print(f" Element at index {index}: {list1[index]}")
    except IndexError:
        print(f" Error: Index {index} is out of range for the list.")
    
list1 = list(map(int, input(" Enter the elements of the list separated by spaces:- ").split()))
index = int(input(" Enter the index to access:- "))

access_element(list1, index)