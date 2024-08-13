# find the sum of the first n natural number

# natutal number using the input function
n = int(input("Enter the number to find the sum of natural no :"))

# Calculate the Sum using formula
sum_of_natural_no = n*(n+1)/2


# calculate sum using a loop
sum =0
for i in range(n+1):
    sum += i
   
print("Sum of N natural no is : ",sum)
print("Sum of N natural no is : ",sum_of_natural_no)