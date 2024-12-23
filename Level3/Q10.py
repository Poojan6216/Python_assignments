def customers_walked_away(N, S):
    occupied = set()
    waiting = set()
    walked_away = 0 

    for customer in S:
        if customer not in occupied and customer not in waiting:
            if len(occupied) < N:
                occupied.add(customer)
            else:
                walked_away += 1
                waiting.add(customer)
        elif customer in occupied:
            occupied.remove(customer)
        elif customer in waiting:
            waiting.remove(customer)

    return walked_away

N = 3
S = "GACCBDDBAGEE"
print("Output:", customers_walked_away(N, S)) 

N = 1
S = "ABCBAC"
print("Output:", customers_walked_away(N, S))
