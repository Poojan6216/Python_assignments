def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count

file_path = 'demo.txt'

result = count_lines_in_file(file_path)
print(f" Number of lines in the file: {result}")