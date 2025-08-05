# Create a Dictionary of Student Marks


student_marks = {'Krishnan': 100, 'Vidya': 99, 'Ivaan': 98, 'Steve Jobs': 100, 'Elon Musk': 99}
print(student_marks)
student_name = input("Enter the student name:")
if student_name in student_marks:
    print(student_name,"'s marks:", student_marks[student_name])
else:
    print("Student ", {student_name}, "not found")