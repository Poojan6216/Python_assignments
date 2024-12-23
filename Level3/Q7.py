def construct_dict_with_loop(students, subjects):
    student_subject_dict = {}
    for i in range(len(students)):
        student_subject_dict[students[i]] = subjects[i]
    return student_subject_dict

def construct_dict_with_comprehension(students, subjects):
    return {students[i]: subjects[i] for i in range(len(students))}

students = ["Sam", "Alice", "Mona"]
subjects = ["Commerce", "Science", "Computer"]

dict_with_loop = construct_dict_with_loop(students, subjects)
print("Output1: ", dict_with_loop)

dict_with_comprehension = construct_dict_with_comprehension(students, subjects)
print("Output2: ", dict_with_comprehension)
