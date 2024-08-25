courseList = []
creditList = []
earnedList = []

def add(course,credit,earn):
    courseList.append(course)
    creditList.append(credit)
    earnedList.append(earn)

def drop(course):
    index = courseList.index(course)
    courseList.pop(index)
    creditList.pop(index)
    earnedList.pop(index)

def printList():
    i=0
    print("{0}   {1}   {2}".format("Course","credit","earned"))
    for course in courseList:
        credit = creditList[i]
        earn = earnedList[i]
        print(f"{course}   {credit}   {earn}")
        i+=1

def cgpa():
    total,totalcredit = 0,0
    i=0
    for credit in creditList:
        earn = earnedList[i]
        total += (credit*earn)
        totalcredit += credit
        i+=1

    return total / totalcredit
