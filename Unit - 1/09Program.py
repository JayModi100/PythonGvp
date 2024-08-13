# Print Fibonacci series

sequence = int(input("How many sequence do you wan't to print? -  "))

a=1
b=0
c = 0


for i in range(sequence):
    print(c,end="   ")
    c = a+b
    a=b
    b=c
    
    