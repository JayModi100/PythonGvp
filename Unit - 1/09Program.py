# Print Fibonacci series

while 1:
    sequence = int(input("How many sequence do you wan't to print? -  "))
    if sequence > 0:
        break
    else:
        print("Please enter positive no")

a=1
b=0
c = 0



for i in range(sequence):
    print(c,end="   ")
    c = a+b
    a=b
    b=c
    
    