def checkPerfectNumber(number):
    sum,list = 0,[]
    for i in range(1,(number // 2)+1):
        if number % i == 0:
            list.append(i)
            sum+=i
    return sum,list
    
    
inputNumber = int(input("Enter the number to check number is perfect or not : "))
result,resultList = checkPerfectNumber(inputNumber)

if result == inputNumber:
    print(f"{result} is perfect number")
    print(f"{result} = ",end=" ")
    
    lenthOfList = len(resultList)
    
    for i in range(lenthOfList):
        print(f"{resultList[i]}",end="")
        
        if (i) != lenthOfList-1:
            print(" + ",end="")  
else:
    print(f"{inputNumber} is not a perfect Number")    
    
print()
print("Print Perferct Number Between 1 to 10000")


for number in range(1,10000):
    result,resultList = checkPerfectNumber(number)

    if result == number:
        print(f"{result} is perfect number")
        print(f"{result} = ",end=" ")
        
        lenthOfList = len(resultList)
        
        for i in range(lenthOfList):
            print(f"{resultList[i]}",end="")
            
            if (i) != lenthOfList-1:
                print(" + ",end="") 
        
        print("")
