def Count(String):
    letters = 0
    numbers = 0
    for i in String:
        if i.isalpha():
            letters +=1
        elif i.isdigit():
            numbers +=1
    
    print(f"Alphabets : {letters} & Number : {numbers}")

String = input(" Enter String ")
Count(String)