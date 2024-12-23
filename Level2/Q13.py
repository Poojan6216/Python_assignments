input_string = input("Enter a string: ")
given_char = input("Enter the character to check: ")

starts_with = lambda string, char: string.startswith(char)

result = starts_with(input_string, given_char)
print(result)
