import datetime

print(" age calculator ")
birth_year = int(input("Enter your year of birth: \n"))
birth_month = int(input("Enter your month of birth: \n"))
birth_day = int(input("Enter your day of birth: \n"))

current_year = datetime.date.today().year
current_month = datetime.date.today().month
current_day = datetime.date.today().day

age_year = current_year - birth_year
age_month = abs(current_month - birth_month)
age_day = abs(current_day - birth_day)

print("Your exact age is: ", age_year, "Years", age_month, "months and", age_day, "days") 
