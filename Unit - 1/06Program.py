student_info = input(" Enter 2 Character of Your Branch \n Enter 2 digit of year \n Enter 1 Character of your Degree \n Enter Roll No \n Ex : CS20M15 \n Enter Your details : ")

branch = student_info[0:2].upper()
year = student_info[2:4]
degree = student_info[4:5].upper()
roll_no = student_info[5:len(student_info)]

if branch == "CS":
    branch = "Computer Science"
    
    if degree == "M":
        degree = "MCA"
    elif degree == "B":
        degree = "BCA"
    elif degree == "P":
        degree = "PGDCA"
    
    print("Student is from Computer Science Department")
    print(f"Branch = {branch}, Year = 20{year}, degree = {degree}, Roll No = {roll_no}")
    
        
