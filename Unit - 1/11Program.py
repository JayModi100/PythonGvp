# Check the positive integer is prime or not

while 1:
    number = int(input("Enter the positive no :"))
    if number >= 2:
        break

i =2
temp = number
while i <= number:
    if number % i == 0:
        if temp == i:
            print(f"{temp} is Prime no.")
        else:
            print(f"{temp} is not Prime no.")
        break;
    i=i+1
    