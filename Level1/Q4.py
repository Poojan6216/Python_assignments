def sum_of_odd_numbers(start, stop):
    sum = 0

    for i in range( start,stop):
        if (i%2 == 1):
            sum += i

    return sum

start = int(input(" Enter starting digit: "))
stop = int(input(" Enter Stoping point: "))

result = sum_of_odd_numbers(start, stop)
print(f"Sum of all odd number: {result}")