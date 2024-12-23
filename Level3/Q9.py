def length_encode(string1):
    encoded_string = ""
    count = 1
    for i in range(1, len(string1)):
        if string1[i] == string1[i-1]:
            count +=1
        else:
            encoded_string += string1[i-1] + str(count)
            count = 1
        
    encoded_string += string1[-1] + str(count)
    return encoded_string

string1 = "wwwaajjjjjebbbkhhh"
output = length_encode(string1)
print(" Encoded String: ", output)