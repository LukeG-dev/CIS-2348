# Luke Gilin
print("Birthday Calculator, numeric values only.")
month = int(input("Enter current month: "))
day = int(input("Enter current day: "))
year = int(input("Enter current year: "))
birthMonth = int(input("Enter birth month: "))
birthDay = int(input("Enter birth date: "))
birthYear = int(input("Enter birth year: "))
age = 0

if day >= birthDay and month >= birthMonth:
    age = year - birthYear
else:
    age = year - birthYear - 1
print()
print("Current day ")
print("Month: ", month)
print("Day: ", day)
print("Year: ", year)
print("Birth day")
print("Month: ", birthMonth)
print("Day: ", birthDay)
print("Year: ", birthYear)
print("You are ", age, " years old.")
if day == birthDay and month == birthMonth:
    print("Happy birthday!")
