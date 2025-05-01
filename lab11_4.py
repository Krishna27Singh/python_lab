import student_management.add_student as add
import student_management.view_student as view
import student_management.update_marks as update


add.add_student("new", 25, 80)
print(view.view_student())

# add.add_student("billa", 25, 0)
# print(view.view_student())

update.update_marks("new",25, 100)
print(view.view_student())

add.add_student("new1", 25, 30)
print(view.view_student())
