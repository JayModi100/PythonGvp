# Collatz sequence
# For even no is divide by 2.
# for odd no is multiply by 3 and add 1.
# repeat until it become 1

no = int(input("Enter the number  :"))

while no != 1:
    if no % 2 == 0:
        no = no // 2
    else:
        no = (no*3)+1

    print(no,end=" ")
        
        