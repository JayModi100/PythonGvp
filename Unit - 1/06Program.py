# Find the student from cs department where the roll no may be in capital or small case letter

while 1:
    student_detail = input("Enter Your Department and Roll number[Department-RollNo] : ").upper();
    print(student_detail)
    if '-' not in student_detail:
        print("Use Format please [Department-RollNo] ")
        continue
    else:
        break

department , roll_no = student_detail.split('-')

if(department == "CS"):
    print("Student is Belong's to Computer Science department")
else:
    print(f"student is Belongs to {department} department")

