# Find birthdays in a month using dictionary
# Birthdays in DD/MM/YY.

months={
1:"January",
2: "February",
3: "March",
4: "April",
5: "May",
6:"June",
7: "July",
8: "August",
9: "September",
10:"October",
11 :"November",
12:"December"
}


while 1:
    day = int(input("Enter data of your birth :"))
    if day <= 0 or day >31:
        print("Please Again fill valid data")
        continue
    break
        
while 1:        
    month = int(input("Enter Month of your birth[only number] :"))
    if month <= 0 or month > 12:
        print("Please Again fill valid month")
        continue
    break

while 1:
    year = int(input("Enter Year of your birth between[1950-2024] :"))
    if year < 1950 or year > 2025:
        print("Please Again fill valid year")
        continue
    break

StrYear = str(year)
birth_month = months[month]
print("Your birth day is in {0} month".format(birth_month))
birth_year = StrYear[-2:]

print(f"Your BirthDate = {day}/{birth_month}/{birth_year}")

