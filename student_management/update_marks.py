from student_management import add_student

student_details = add_student.student_details


def update_marks(name, roll, marks):
    
    print(student_details[name])
    # print(type(student))
    if(student_details[name][roll]==roll):
        student_details[name][marks]=marks
            