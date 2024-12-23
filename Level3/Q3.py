def JtoI(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    corrected_content = content.replace('J', 'I')

    print("Corrected content:")
    print(corrected_content) 

file_path = 'Words.txt'
JtoI(file_path)