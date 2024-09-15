# Write the program to find out if the two blood group match.

# Take a blood group from user
bloodGroups = ["A+","A-","B+","B-","O+","O-","AB+","AB-"]

while True:
    person1Blood = input("Enter the Blood Group")
    if person1Blood in bloodGroups:
        break
    else:
        print("Please Valid Blood group enter")
        
while True:
    person2Blood = input("Enter the Blood Group")
    if person2Blood in bloodGroups:
        break
    else:
        print("Please Valid Blood group enter")
    
if person1Blood == person2Blood:
    print("Blood Group are match.")
else:
    print("Blood Group are not Match.")
