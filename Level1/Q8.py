def GCD (a,b):
    while b:
        a, b = b, a % b
    return a

def LCM (a,b):
    lcm = (a * b) / GCD(a,b)
    return lcm

a = int(input(" Enter the first number:- "))
b = int(input(" Enter the second number:- "))

result = LCM (a,b)
print(f" LCM of {a} and {b} is : {result}")