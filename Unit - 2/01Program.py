# number = int(input("Enter the number : "))
# list = []
# for i in range(1,(number//2)+1):
#     if(number % i == 0):
#         list.append(i)
#         # print(list)

# sum=0
# for i in list:
#     sum+=i

# if(sum == number):
#     print(f"{number} is perfect no It's {sum}")
# else:
#     print(f"{number} is not perfect no {sum}")


for No in range(5,10000):
    list = []
    for i in range(1,(No//2)+1):
        if(No % i == 0):
            list.append(i)
            # print(list)

    sum=0
    for i in list:
        sum+=i

    if(sum == No):
        print(f"{No} {sum}")
    