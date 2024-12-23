def reverse_number(number):
    num = 0
    while number > 0:
        digit = number % 10
        num = num * 10 + digit
        number = number // 10
    return num

number = int(input(" Enter the number:- "))
result = reverse_number(number)
print("Reserveed number: ", result)