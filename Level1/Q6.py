def Perfect_Number(number):
    sum = 0
    for i in range(1, number):
        if number% i  == 0:
            sum += i
        
    return sum

number = int(input(" Enter number to check whethe it's perfect or not:  "))
result = Perfect_Number(number)

if result == number:
    print(f" yes ")
else:
    print(" No ")