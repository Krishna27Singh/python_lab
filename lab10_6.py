file = open("marks.txt", "r")
lines = file.readlines()

total_marks = 0
count = 0

for line in lines[1:]:
    data = line.split(',')
    print(data[2])
    marks = int(data[2])
    total_marks += marks
    count += 1

    if marks>80:
        top_students = open("top_students.txt", "a")
        top_students.write(data[1]+" ")

print("average marks", total_marks/count)