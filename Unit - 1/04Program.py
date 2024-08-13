# Word shuffle using string manipulation

WordStr = "Hello I am One Line String For Suffle "

list = WordStr.split(" ")
list1 = ""
mid = len(list)//2

for i in range(mid):
    list1+=list[i]
    list1+=" "
    list1+=list[mid+i]
    list1+=" " 
    
print(list1)