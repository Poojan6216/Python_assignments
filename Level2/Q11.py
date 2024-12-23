def split_characters(string):
    return list(string)

string = input(" Enter words separated by spaces: ").split()

new_list = list(map(split_characters, string))
print(new_list)