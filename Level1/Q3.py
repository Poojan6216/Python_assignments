def grad_calculator():
    physics = float(input(" Enter Physics score: "))
    chemistry = float(input("Enter Chemistry score: "))
    biology = float(input("Enter Biology score: "))
    mathematics = float(input("Enter Mathematics score: "))
    computer = float(input("Enter Computer score: "))

    total_marks = physics + chemistry + biology + mathematics + computer
    percentage = (total_marks / 500) * 100

    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    elif percentage >= 40:
        grade = "E"
    else:
        grade = "F"
    
    print(f"Percentage: {percentage}")
    print(f"Grades: {grade}")

grad_calculator()
