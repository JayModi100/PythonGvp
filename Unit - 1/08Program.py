# Teacher enter the marks and mark is atleast 40 for pass. Teacher want's to check how many no of student is pass.

students=int(input("How Many Students : "))
p=0
i=1

while(i<=students):
    m=int(input("Enter {} Student Marks : ".format(i)))

    if(m>100 or m<0):
        print("please,enter valid student marks")
        continue

    if(m>=40):
        p+=1
    i+=1    

percentage = (p*100)/students

print("Percantage of Passing Students is {}%".format(percentage))

    