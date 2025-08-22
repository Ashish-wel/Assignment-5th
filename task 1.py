# Task 1: Create a Dictionary of Student Marks


student_marks = {
    "Alice": 85,
    "Bobby": 78,
    "Chandu": 92,
    "Danish": 74,
    "Evishka": 90
}


name = input("Enter the student's name: ")


if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")

-- output --

Enter the student's name: Alice
Alice's marks: 85
