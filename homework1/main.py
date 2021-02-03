# Luke Gilin
print("Birthday Calculator, numeric values only.")
# Get input from user with prompt
month = int(input("Enter current month: "))
day = int(input("Enter current day: "))
year = int(input("Enter current year: "))
birthMonth = int(input("Enter birth month: "))
birthDay = int(input("Enter birth date: "))
birthYear = int(input("Enter birth year: "))

age = 0  # Declare age variable

if day >= birthDay and month >= birthMonth:  # Check month and year to find age
    age = year - birthYear
else:
    age = year - birthYear - 1

#  Print output

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
if day == birthDay and month == birthMonth:  # Check if it is user's birthday
    print("Happy birthday!")
