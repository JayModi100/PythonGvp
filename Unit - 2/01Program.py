number = int(input("Enter the number : "))
sum=0

for i in range(1,(number//2)+1):
    if(number % i == 0): 
        sum+=i
        

if(sum == number):
    print(f"{number} is perfect no It's {sum}")
else:
    print(f"{number} is not perfect no {sum}")
