def power_of_two(n):
    if n<= 0:
        return False
    if n == 1:
        return True
    return n % 2 == 0 and power_of_two(n//2)

number = int(input(" Enter a Number:- "))

if power_of_two(number):
    print(f"{number} is a power of two.")
else:
    print(f"{number} is not a power of two.")