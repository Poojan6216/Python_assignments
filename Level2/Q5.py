Temperature_readings = list(map(int, input(" Enter temperature readings separated by spaces").split()))

average_temp = sum(Temperature_readings) / len(Temperature_readings)
highest_temp = max(Temperature_readings)
lowest_temp = min(Temperature_readings)

print(f" Average Temperature: {average_temp:.1f}")
print(f" Highest Temperature: {highest_temp}")
print(f" Lowest Temperature: {lowest_temp}")
