def frequency_count(list):
    frequency = {}

    for element in list:
        if element in frequency:
            frequency[element] += 1 
        else:
            frequency[element] = 1

    return frequency

list = input (" Enter a list of numbers separated by spaces: ").split()
list = [int(num) for num in list]
count = frequency_count(list)

print("Frequency count:", count)