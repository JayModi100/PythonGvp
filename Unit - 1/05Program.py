# Write the program to find out if the two blood group match.

# Take a blood group from user
boolGroup1=input("Enter First Person Blood : ").upper()
boolGroup2=input("Enter Second Person Blood : ").upper()


# Compare the blood group
if(boolGroup1 == boolGroup2):
    print("Blood Group is match")
else:
    print("Blood Group is not match")