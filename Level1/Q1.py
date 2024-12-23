def num(a):
    if (a%3 == 0 and a%5 == 0):
        print("ConsultAdd Python Training")
    elif (a%5 == 0):
        print("PythonTraining")
    elif (a%3 == 0):
        print("ConsultAdd")

number = int(input("Enter number to check"))
num(number)