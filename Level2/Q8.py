def vowels_count(string):
    vowels = "aeiouAEIOU"
    count = 0

    for i in string:
        if i in vowels:
            count +=1
        
    return count

string =  input("Enter a string:- ")
result = vowels_count(string)
print(f" Number of vowels: {result}")