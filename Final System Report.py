# The array below stores the student data entered by the user.
management_systems = []
# The function below controls the input of the students data with conditions assigned to them.


def my_fun():
    # The function below checks the name input from the user
    def namechecker():
        if not name.isalpha():   # Checks the name input to be alphabets only, don't leave space when entering name
            print("Oops!! Please enter alphabets only \n No space when entering name")
            breakpoint()
        else:
            print("proceed")
        return

    # The function below checks the index number input from the user
    def indexchecker():
        while index_number.isalpha() or len(index_number) < 10:
            # index number must be integers only and  greater than or equal to 10 digits
            print("Ooops!!! enter integers only \n Check!! index number length >= 10")
            breakpoint()
        else:
            print("Proceed")
        return

    # The function below checks the course input from the user
    def coursechecker():
        if not course.isalpha():   # enter alphabets only, no space when entering course
            print("Error!!! enter alpha characters only and don't leave space when entering course")
            breakpoint()
        else:
            print("Proceed")
        return

    # The function below checks the amount input from the user
    def amountchecker():
        while amount_paid > total_fees:
            print("Student will receive credit balance of" + " " + str(amount_paid - total_fees))
            break
        else:
            print("Proceed")
        return

    # The function below adds the information entered into the management_systems
    def student_info():
        management_systems.insert(a, {
            'name': name, 'index_number': index_number, 'course': course, 'total_fees': total_fees,
            'amount_paid': amount_paid,
            'fees_balance': fees_balance
        })
        return

    # Student Information Input
    name = input("Please Enter name: ")
    namechecker()
    index_number = input("Please Enter Index Number: ")
    indexchecker()
    course = input("Please Enter Program: ")
    coursechecker()
    total_fees = float(input("Please Enter total fees: "))
    amount_paid = float(input("Please Enter amount paid: "))
    amountchecker()
    # Checks the balance after payment
    fees_balance = amount_paid - total_fees
    # The codes below checks the addition of student information into the management_systems
    # By looping the index(a) of each student data entered from index 0 to 4. (5 Consecutive times)
# The codes below loops(i) the student- data to be entered 5 times
    a = 0
    while a < 5:
        a += 1

    student_info()


i = 12
while i <= 5:
    my_fun()
    i += 1

print("THE STUDENT MANAGEMENT REPORT")

indexes = "INDEX NUMBER"
nam = "STUDENT NAME"
job = "PROGRAM OFFERED"
total = "TOTAL FEES"
amt = "AMOUNT PAID"
bal = "BALANCE"
print("{:<15} {:<13} {:<15} {:<13} {:<13} {:<13}".format(nam, indexes, job, total, amt, bal))
# The code below loops all the data stored in the management_systems.
for management_system in management_systems:
    print("{:<15} {:<13} {:<15} {:<13.2f} {:<13.2f} {:<13.2f}".format(management_system['name'],
        management_system['index_number'],
        management_system['course'],
        management_system['total_fees'],
        management_system['amount_paid'],
        management_system['fees_balance']))



