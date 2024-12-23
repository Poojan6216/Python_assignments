def count_pairs(N, k):
    count = 0
    n = len(N) 

    for i in range(n):
        for j in range(i + 1, n):
            if N[i] + N[j] == k:
                count +=1
            
    return count

N = list(map(int, input(" Enter elements of the array separated by spaces:- ").split()))
k = int(input(" Enter the target sum (k):- "))

result = count_pairs(N, k)
print(" Pair count", result)