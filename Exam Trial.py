def calculate_grade(mark):
    if mark >= 70 and mark <= 100:
        return 'A'
    elif mark >= 60 and mark <= 69:
        return 'B'
    elif mark >= 50 and mark <= 59:
        return 'C'
    elif mark >= 40 and mark <= 49:
        return 'D'
    elif mark >= 0 and mark <= 39:
        return 'F'
    else:
        return 'Invalid Mark'

# Dictionary to store student marks
student_marks = {}


# Input marks for each student
num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    student_name = input(f"Enter the name of student {i+1}: ")
    accounting_mark = int(input(f"Enter the mark for Accounting: "))
    economics_mark = int(input(f"Enter the mark for Economics: "))
    mathematics_mark = int(input(f"Enter the mark for Mathematics: "))
    english_mark = int(input(f"Enter the mark for English: "))
    student_marks[student_name]= {
        'accounting': accounting_mark,
        'economics': economics_mark,
        'mathematics': mathematics_mark,
        'english': english_mark
    }

edin = "STUDENT NAME"
program = "COURSE"
score = "MARK"
CWA = "GRADE"
# Calculate and display grades for each student
print("\nGrades for each student:")
print("{:<15}{:<14}{:<14}{:<14}.".format(edin, program, score, CWA))
for student_name, marks in student_marks.items():
    print("\n")
    for course, mark in marks.items():
        # print(f"\nStudent: {student_name}")
        grade = calculate_grade(mark)
        print("{:<15}{:<14}{:<14}{:<14}".format(student_name, course, mark, grade))
        # print(f"{course}: Mark = {mark}, Grade = {grade}")
