# print the list a recursively
def printListRecursively(lis):
    for item in lis:
        if isinstance(item,(list)):
            printListRecursively(item)
        else:
            print(item)


lis = [1,[2,[3,4],5],6,7]
printListRecursively(lis)


