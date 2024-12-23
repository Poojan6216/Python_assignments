def even_length_words(file_path):
    with open(file_path, 'r') as file:
        result_lines = []
        for line in file:
            words = line.split() 
            even_words = [word for word in words if len(word) % 2 == 0]
            result_lines.append(' '.join(even_words)) 

    return '\n'.join(result_lines) 

file_path = 'doc.txt'

even_length_content = even_length_words(file_path)
print("Content with even-length words only:")
print(even_length_content)
