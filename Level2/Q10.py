def stone_piles(n):
    piles = []
    start = 2 if n % 2 == 0 else 1

    while start < n:
        piles.append(start)
        start += 2
    
    return piles

n = int(input(" Enter the number of stones in the first pile (n): "))

result = stone_piles(n)
print(f" Stones in a single pile = {result}")