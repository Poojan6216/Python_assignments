def Factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

number = int(input(" Enter positive number: "))
result = Factorial(number)
print(f" Factorial for given number : {result}")