def rotate_array(N, d):
    n = len(N)
    d = d % n
    new_array = N[-d:] + N[:-d]
    return new_array

N = list(map(int, input(" Enter the elemnets of array, separated by space:- ").split()))
d = int(input(" Enter the number you want to rotate (D):- "))

result = rotate_array(N,d)
print(" Array after rotations: ", result)