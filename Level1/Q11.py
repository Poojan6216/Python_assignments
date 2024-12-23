def sum_of_digits(number):
    while number >= 10:
        sum = 0 
        while number > 0:
            sum += number % 10
            number //= 10 
        number = sum
    return number

number = int(input(" Enter a number:- "))

output = sum_of_digits(number)
print(" Final single-digit sum  ", output)